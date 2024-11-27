#!/usr/bin/env sh

docker run \
    --rm -it \
    -e DOCKERFILE_PATH=/build \
    -v $PROJECT_DIR:/build \
    -v /var/run/docker.sock:/var/run/docker.sock \
    ci_container:latest ci build -t ci_container:latest
