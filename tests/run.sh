#!/usr/bin/env sh

PROJECT_DIR=/mnt/c/Users/ratio/Proyectos/nekops

docker build .. -t lifecycle_lib:latest
docker run \
    --rm -it \
    -e PHASE=integration \
    -e STAGE=build \
    -e TAG=test_container \
    --mount type=bind,source=$PROJECT_DIR/tests,target=/build,readonly \
    -v /var/run/docker.sock:/var/run/docker.sock \
    lifecycle_lib:latest