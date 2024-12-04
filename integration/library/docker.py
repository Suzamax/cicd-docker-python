import os
import docker
import logging
import docker.errors
from rich.logging import RichHandler
from common.logs import LogsLib


class DockerLib(LogsLib):
    def __init__(self, loglevel) -> None:
        self.client = docker.client.from_env()
        super().__init__(loglevel)

    def build(self, tag, dockerfile):
        self.log.info("Building %s container..." % tag)
        try:
            image, logs = self.client.images.build(
                path=os.environ['BUILD_PATH'],
                tag=tag, timeout=900,
                dockerfile=dockerfile)
            if image:
                for chunk in logs:
                    if 'stream' in chunk:
                        for line in chunk['stream'].splitlines():
                            self.log.debug(line)
            self.log.info("Container built successfully!")
        except docker.errors.BuildError as e:
            self.log.error("Errors while building the container:")
            self.log.error(e)
    
    def push(self, tag, repo):
        self.self.log.info("Pushing %s to %s..." % tag, repo)
        try:
            resp = self.client.images.push(repo, tag, stream=True, decode=True)
            for line in resp:
                self.log.debug(line)
            self.log.info("Container pushed successfully!")
        except docker.errors.APIError as e:
            self.log.error("Errors while pushing the container:")
            self.log.error(e)