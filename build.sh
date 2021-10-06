#!/bin/bash
echo "Deleting running containers"

docker stop $(docker ps -q --filter ancestor=vladisbot )
docker rm $(docker ps -q --filter ancestor=vladisbot )

echo "Removing dangling images"
docker images -f “dangling=true” -q

echo "Running build"
docker build . --tag vladisbot