import subprocess
from common.logs import LogsLib


class AnsibleLib(LogsLib):
    def __init__(self, loglevel) -> None:
        super().__init__(loglevel)

    def playbook(self):
        pass