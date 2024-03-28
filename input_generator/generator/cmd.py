import subprocess

from .generator import Generator


class CMD(Generator):
    def __init__(self, cmd):
        self.cmd = cmd

    def gen(self):
        subprocess.run(self.cmd.split())
