from typing import Optional

import typer
from typing_extensions import Annotated

from .generator.int import Int
from .subcommands.file import app as app_file
from .subcommands.permutation import app as app_permutation
from .subcommands.string import app as app_string

app = typer.Typer()

app.add_typer(app_string, name="string")
app.add_typer(app_permutation, name="permutation")
app.add_typer(app_file, name="from-file")


@app.command("int")
def gen_int(
    low: int,
    high: int,
    log_scale: Annotated[bool, typer.Option("--log-scale")] = False,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    int_ = Int(low, high, log_scale, seed=seed)
    print(int_())


if __name__ == "__main__":
    app()
