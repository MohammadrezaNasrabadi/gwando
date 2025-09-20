## Auto-Quarantine Steps:

If the worker issued a url with strics access (like CAPTHCA challenge, Basic Authentication, etc) the healtcheck status of the container changes to `unhealthy`.

```bash
# docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS                     PORTS                                         NAMES
b3d0631c2a7d   gwando:latest        "uvicorn main:app --…"   3 minutes ago   Up 3 minutes (unhealthy)   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   gwando
```

In such cases, We can restart the container to continue crawling remaining URLs.

The procedure can be automated by using a simple bash script and cronjob

## Auto-Replace

The process can be done by stopping and removing the worker container and removing the related docker image. Then, We can build the new version of worker image and re create the worker container.
