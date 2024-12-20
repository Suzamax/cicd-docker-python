FROM alpine:3.20

RUN apk add --no-cache --update \
    python3 \
    py3-pip \
    opentofu \
    ansible \
    git \
    curl \
    wget \
    openssl \
    openssh

RUN curl -L -k -g -o /usr/local/bin/jf "https://releases.jfrog.io/artifactory/jfrog-cli/v2-jf/%5BRELEASE%5D/jfrog-cli-linux-amd64/jf" \
    && chmod +x /usr/local/bin/jf

WORKDIR /app
COPY infrasctructure/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY infrastructure/ /app
COPY common/ /app
ENTRYPOINT [ "/app/__main__.py" ]