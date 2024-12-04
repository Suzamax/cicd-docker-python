FROM python:3.13-alpine

RUN apk add --no-cache --update \
    docker-cli \
    docker-cli-buildx \
    git \
    curl \
    wget \
    openssl \
    openssh

RUN curl -L -k -g -o /usr/local/bin/jf "https://releases.jfrog.io/artifactory/jfrog-cli/v2-jf/%5BRELEASE%5D/jfrog-cli-linux-amd64/jf" \
    && chmod +x /usr/local/bin/jf

WORKDIR /app
COPY integration/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY integration/ /app
COPY common/ /app/common
ENTRYPOINT [ "/app/__main__.py" ]