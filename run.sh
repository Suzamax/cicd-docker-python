#!/usr/bin/env sh

docker build . -t lifecycle_lib:latest
docker run \
    --rm -it \
    -v $PROJECT_DIR:/build \
    -v /var/run/docker.sock:/var/run/docker.sock \
    lifecycle_lib:latest ci build -t test_container