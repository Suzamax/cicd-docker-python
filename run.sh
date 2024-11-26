#!/usr/bin/env sh

docker run \
    --rm -it \
    -v $PROJECT_DIR:/build \
    -v /var/run/docker.sock:/var/run/docker.sock \
    test_container:latest ci build -t test_container:latest
