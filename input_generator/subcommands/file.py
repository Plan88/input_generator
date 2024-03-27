from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ..generator.pyfile import PyFile

app = typer.Typer()


@app.command()
def python(
    path: Path,
    stdin: Annotated[Optional[Path], typer.Option()] = None,
    stdout: Annotated[Optional[Path], typer.Option()] = None,
):
    pyfile = PyFile(path)
    pyfile(stdin=stdin, stdout=stdout)
