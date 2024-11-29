import subprocess
import logging
from library.logs import LogsLib
from rich.logging import RichHandler

FORMAT = "%(message)s"

class OpentofuLib(LogsLib):
    def __init__(self, loglevel) -> None:
        super().__init__(loglevel)

    def opentofu_plan(self):
        self.log.info("Planning infrastructure...")
        output = subprocess.run([
            'tofu',
            'plan'
        ], check=True, capture_output=True, text=True).stdout

        """
        At this point we might just stop the pipeline and ask permission
        to the user to continue, as this may be nuclear. Might as well add
        infracost in order to check the expenses.
        """

    def opentofu_apply(self):
        self.log.info("Applying infrastructure...")
        output = subprocess.run([
            'tofu',
            'apply'
        ], check=True, capture_output=True, text=True).stdout