#!/usr/bin/env sh

PROJECT_DIR=/HOST/path/is/there

docker build .. -t lifecycle_lib:latest
docker run \
    --rm -it \
    -e PHASE=integration \
    -e STAGE=build \
    -e TAG=test_container \
    -v $PROJECT_DIR/tests:/build \
    -v /var/run/docker.sock:/var/run/docker.sock \
    lifecycle_lib:latest
