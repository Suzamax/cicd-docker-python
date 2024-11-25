import docker
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

class DockerLib:
    def __init__(self) -> None:
        self.client = docker.client.from_env()


    def build(self, tag):
        log.info("Starting container build...")
        problems = []
        try:
            image, logs = self.client.images.build(path="/build", tag=tag, timeout=900)
            if image:
                for chunk in logs:
                    if 'stream' in chunk:
                        for line in chunk['stream'].splitlines():
                            log.debug(line)
        except docker.errors.BuildError as e:
            problems.append(e)
        finally:
            if len(problems) > 0:
                log.error("Errors while building the container:")
                [log.error(problem) for problem in problems]
            else:
                log.info("Container built successfully!")


    def prune(self):
        return self.client.images.prune_builds()