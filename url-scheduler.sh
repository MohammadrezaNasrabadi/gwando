#!/bin/bash

URL=$1

docker exec -it redis redis-cli PUBLISH ${REDIS_CHANNEL_NAME:-gwando} "{\"url\": \"${URL}\"}"
