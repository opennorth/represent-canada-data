# Docker

## Setup

    cd ./docker && ./deploy.sh

The first time you run ./deploy.sh, it might take several minutes, but will take a few seconds on future runs.

## Destroying the environment

    docker-compose down

## Opening a shell

Once Docker is set up (deployed), open a shell like this:

    cd ./docker && docker-compose exec represent /bin/bash

## Usage
