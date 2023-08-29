# hello-world-app
This is a multi-container app based on documentation for [docker compose](https://docs.docker.com/compose/gettingstarted/). The app pulls a ramdon meme from the following [reddit api](https://github.com/D3vd/Meme_Api). One container serves as a redis database to cache the total amount of memes shown to the user. The front end of the app is built using flask, html, and css. It is hosted on a Linux Alpine container.

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

You should see a meme, the subreddit it is taken from, and the amount of memes you have seen thus far.

## License
Distributed under the MIT License. See `LICENSE` for more information.