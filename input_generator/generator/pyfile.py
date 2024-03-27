import subprocess
from pathlib import Path

from .generator import Generator


class PyFile(Generator):
    def __init__(self, path: Path, seed: int | None = None):
        self.path = path

    def gen(self, stdin: Path | None = None, stdout: Path | None = None):
        cmd = f"python3 {str(self.path)}"
        kwargs = {}
        if stdin is not None:
            kwargs["stdin"] = open(stdin, "r")
        if stdout is not None:
            kwargs["stdout"] = open(stdout, "w")

        subprocess.run(cmd.split(), **kwargs)
