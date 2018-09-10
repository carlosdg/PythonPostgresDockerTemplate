# Python, PostgreSQL, Docker template

A simple template for a project using Python and PostgreSQL with Docker. Using the `psycopg2-binary` package for connecting to the database

## Prerequisites

At a very high level you'll only need to have docker installed and this repository downloaded.

## Use

First add an `app.env` file with all the environment variables needed for the app. You can find the main ones in `app.env.example`:
  - __APP_DB_NAME__: Database name that the application will use
  - __APP_DB_USER__: Database user name that the application will use to connect to the database
  - __APP_DB_USER_PASSWORD__: Database user password that the application will use to connect to the database
  - __APP_DB_HOST__: Host where the database is located. By using `docker-compose` all the containers will be connected and, in the application container, we can refer to the database container with the __`db` DNS name__ (because we called the database conteiner `db` in the `docker-compose.yml` file)
  - __APP_DB_PORT__: Port where the database will be listening to. When using `docker-compose` we can connect to the __port 5432__ because we are exposing it to other containers

Then add an `db.env` file with all the environment variables needed for the app. You can find more information at [the `Environment Variables` section of the `postgres` image at hub.docker.com](https://hub.docker.com/_/postgres/)

Run `docker-compose up db` to run the database

Run `docker-compose up app` to run the application. Note that the entry point is `src/main.py` because it is defined that way via the `command` property of `app` in the `docker-compose.yml` file.