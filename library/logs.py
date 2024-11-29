import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"

class LogsLib:
    def __init__(self, loglevel) -> None:
        logging.basicConfig(
            level=loglevel, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
        )
        self.log = logging.getLogger("rich")