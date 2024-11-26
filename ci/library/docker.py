import docker
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"


class DockerLib:
    def __init__(self, logLevel) -> None:
        self.client = docker.client.from_env()
        logging.basicConfig(
            level=loglevel, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
        )
        self.log = logging.getLogger("rich")

    def build(self, tag):
        self.self.log.info("Starting container build...")
        problems = []
        try:
            image, logs = self.client.images.build(path="/build", tag=tag, timeout=900)
            if image:
                for chunk in logs:
                    if 'stream' in chunk:
                        for line in chunk['stream'].splitlines():
                            self.log.debug(line)
        except docker.errors.BuildError as e:
            problems.append(e)
        finally:
            if len(problems) > 0:
                self.log.error("Errors while building the container:")
                [self.log.error(problem) for problem in problems]
            else:
                self.log.info("Container built successfully!")

    def prune(self):
        return self.client.images.prune_builds()
