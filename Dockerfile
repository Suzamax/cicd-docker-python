FROM docker.io/python:3.13-alpine

RUN apk add --no-cache docker-cli bash

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./ci /app

ENTRYPOINT [ "/app/entrypoint.sh" ]