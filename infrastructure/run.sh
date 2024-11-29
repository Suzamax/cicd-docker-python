#!/usr/bin/env sh

docker run \
    --rm -it \
    -v $PWD:/build \
    iac_container:latest terraform plan