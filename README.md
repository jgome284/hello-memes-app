# hello-world-app
This is a multi-container app that counts page views and displays a simple print statement. It is based on documentation for [docker compose](https://docs.docker.com/compose/gettingstarted/).

## Prerequisites
To start, you need to have Docker Engine and Docker Compose on your machine. You can either:
* Install Docker Desktop which includes both Docker Engine and Docker Compose
* Install Docker Engine and Docker Compose as standalone binaries

You don't need to install Python or Redis, as both are provided by Docker images.

## Getting started
From your project directory, start the application by running:
```sh
docker compose up
```

Enter http://localhost:8000/ in a browser to see the application running. Otherwise, if this doesn't resolve, you can also try http://127.0.0.1:8000.

You should see a message in your browser saying:

> Hello World! I have been seen 1 times.
