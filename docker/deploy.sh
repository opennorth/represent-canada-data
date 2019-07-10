#!/bin/bash
#
# Set up a Docker environment.
#
set -e

echo "Setting up a Docker environment."

docker pull ubuntu:17.10
docker-compose build
docker-compose up -d
docker-compose exec represent /bin/bash -i -c '
pip3 install -r requirements.txt flake8
npm install -g esri-dump'

echo ""
echo "Everything seems up and running."
echo ""
echo "Please refer to ./docker/README.md for usage."
echo ""
