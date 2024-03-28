from typing import Optional

import typer
from typing_extensions import Annotated

from .generator.cmd import CMD
from .generator.int import Int
from .subcommands.permutation import app as app_permutation
from .subcommands.string import app as app_string

app = typer.Typer()

app.add_typer(app_string, name="string")
app.add_typer(app_permutation, name="permutation")


@app.command("int")
def gen_int(
    low: int,
    high: int,
    log_scale: Annotated[bool, typer.Option("--log-scale")] = False,
    seed: Annotated[Optional[int], typer.Option()] = None,
):
    int_ = Int(low, high, log_scale, seed=seed)
    print(int_())


@app.command("from-cmd")
def from_cmd(cmd: str):
    cmd_ = CMD(cmd)
    cmd_()


if __name__ == "__main__":
    app()
