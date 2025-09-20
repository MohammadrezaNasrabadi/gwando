# GWANDO

Crocodylus is always crawling!

`gwando` is a simple and scalable web crawling system developed in `python`.

## Architecture

The system is composed of several services. `url-scheduler` is a simple bash script reads the URL to be crawled as input and publishes to `redis` message queue.

`redis` is used to store non-processed urls as a message queue service.

`gwando`, as a worker, is subscribed to the redis channel and read the urls to be crawled from redis channel.

Finally, when the processing procedure is done, the processed data is stored on `postgres` database.

At this time, the processing procedure fetches the existing URLs in html type of the processed URL and stores them alongside the status code to database.

```sql
                +-------------------+
                |   URL Scheduler   |
                +---------+---------+
                          |
                          v
              +-----------------------+
              |     Queue (redis)     |
              +-----------------------+
                          |
                          v
                +-------------------+
                |  Worker (gwando)  |
                +-------------------+
                          |
                          v
           +-----------------------------+
           |   Data Storage (postgres)   |
           +-----------------------------+
```

## Getting Started

### Prerequisites
Before bringing up the services, make sure you have installed `docker` and `docker compose`.

### Setup

1. **Clone the repository.**

```bash
git clone <repository-url>

cd gwando
```

2. **Create the environment file.**

Copy the `.env.example` file to new file named `.env` and update it with your desired setup. There is no essential need to replace and change the environment variables; because it will be habdled by default variables in codebase.

3. **Build and run the services**

```bash
docker compose up -d
```

After the setup was completed and all services are up and running, the Worker will be available on `http://127.0.0.1:8000`

4. **Pubish URL to redis**

URLs to be crawled can be published to redis via `url-scheduler.sh` script. For example:

```bash
./url-scheduler.sh https://google.com
```

## Configuration

The application is configured using environment variables. The supported variables are as below:


| Variable                  | Description                                                              | Default Value                               |
| ------------------------- | ------------------------------------------------------------------------ | ------------------------------------- |
| `DATABASE_HOST`           | The hostname of the postgres database.                    | `postgres`                           |
| `DATABASE_USER`           | The username for the postgres database. database.                                | `postgres`                                |
| `DATABASE_PASSWORD`       | The password for the postgres database.                                | `password`                            |
| `DATABASE_NAME`             | The name of the postgres database.                                     | `gwando`                                |
| `REDIS_HOST`              | The hostname of the redis server.                                        | `redis`                               |
| `REDIS_CHANNEL_NAME`         | The redis channel name.                               | `gwando`                                   |


## Metrics

The application metrics is available on `http://127.0.0.1:8000/metrics` endpoint.

There is supported prometheus metrics inside the project:

| Name                | Exposed informations                   |
|---------------------|----------------------------------------|
| `crawler_fetch_total`     | Total number of crawler fetches. |
| `crawler_success_total` | Number of successful crawler fetches.     |
| `crawler_error_total` | Number of failed crawler fetches.     |

## Healthcheck

The healthy status of the worker can be obtained via `http://127.0.0.1:8000/healthy` endpoint.

The expected output should be in below format:

```json
{"status":true,"date":"2025-09-20T14:45:34.065839"}
```
If the worker goes to unhealthy state, the `status` will be shown as `false`.

