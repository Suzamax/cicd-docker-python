FROM alpine:3.20

RUN apk add --update --no-cache \
    python3 \
    py3-pip \
    kubectl \
    helm \
    yq \
    docker-compose \
    docker-cli \
    docker-cli-buildx \
    git \
    wget \
    curl \
    bash

RUN curl -L -k -g -o /usr/local/bin/jf "https://releases.jfrog.io/artifactory/jfrog-cli/v2-jf/%5BRELEASE%5D/jfrog-cli-linux-amd64/jf" \
    && chmod +x /usr/local/bin/jf