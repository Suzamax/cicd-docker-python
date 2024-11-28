#!/usr/bin/env sh

docker run \
    --rm -it \
    -v $PWD:/workdir \
    iac_container:latest terraform plan