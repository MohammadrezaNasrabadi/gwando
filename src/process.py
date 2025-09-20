from postgres.insert_db import insert_db
from prometheus import metrics
from custom_logger import get_custom_logger
from postgres.schema import Data

import redis.asyncio as redis
import requests
import json
import os


from bs4 import BeautifulSoup


logger = get_custom_logger(__name__)


redis_channel_name = os.getenv('REDIS_CHANNEL_NAME', 'gandoo')
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.StrictRedis(host=redis_host, port=6379)


def _get_included_urls(content):
    urls = []
    soup = BeautifulSoup(content, 'html.parser')
    anchor_tags = soup.find_all('a')
    for tag in anchor_tags:
        href = tag.get('href')
        if href:
            urls.append(href)
    return urls


async def _fetch_url(map):
    data = json.loads(map)
    url = data['url']
    included_urls = None
    status_code = None
    logger.debug(f'processing the url {url}.')
    metrics.CRAWLER_FETCH_TOTAL.inc()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(f'url {url} successfully fetched.')
            included_urls = _get_included_urls(response.content)
            metrics.CRAWLER_SUCCESS_TOTAL.inc()
        else:
            logger.warn(f'could not fetch the url {url}.')
            included_urls = []
            metrics.CRAWLER_ERROR_TOTAL.inc()
        status_code = response.status_code
    except Exception as e:
        logger.error(f'failed to fetch the url {url}.')
        metrics.CRAWLER_ERROR_TOTAL.inc()

    data = {
        "url": url,
        "included_urls": included_urls,
        "status_code": status_code
    }

    await insert_db(Data.parse_obj(data))


async def start_process():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(redis_channel_name)

    logger.debug(f'subscribed to the redis channel: {redis_channel_name}.')
    async for message in pubsub.listen():
        if message['type'] == 'message':
            await _fetch_url(message['data'].decode('utf-8'))
