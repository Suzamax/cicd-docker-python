FROM docker.io/python:3.13-alpine

RUN apk add --no-cache --update \
    helm \
    kubectl \
    curl

RUN curl -L -k -g -o /usr/local/bin/jf "https://releases.jfrog.io/artifactory/jfrog-cli/v2-jf/%5BRELEASE%5D/jfrog-cli-linux-amd64/jf" \
    && chmod +x /usr/local/bin/jf

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "/app/__main__.py" ]