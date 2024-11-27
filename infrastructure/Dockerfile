FROM alpine:3.20

RUN apk add --no-cache --update \
    opentofu \
    ansible \
    git \
    curl \
    wget \
    openssl \
    openssh

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY src/ /app
ENTRYPOINT [ "/app/__main__.py" ]