from typing import Optional

import typer
from typing_extensions import Annotated

from ..generator.int import Int
from ..generator.permutation import Permutation
from ..utils import next_seed

app = typer.Typer()


@app.command()
def vec(
    min_len: int,
    max_len: int,
    zero_indexed: Annotated[bool, typer.Option("--zero-indexed")] = False,
    no_display_length: Annotated[bool, typer.Option("--no-display-length")] = False,
    seed: Optional[int] = None,
):
    int_ = Int(min_len, max_len, seed=seed)

    length = int_()
    permutation = Permutation(zero_indexed, seed=seed)
    generated = permutation(length=length)

    if not no_display_length:
        print(length)
    print(*generated)


@app.command()
def mat(
    min_height: int,
    max_height: int,
    min_width: int,
    max_width: int,
    zero_indexed: Annotated[bool, typer.Option("--zero-indexed")] = False,
    no_display_length: Annotated[bool, typer.Option("--no-display-length")] = False,
    seed: Optional[int] = None,
):
    intH = Int(min_height, max_height, seed=seed)
    intW = Int(min_height, max_height, seed=next_seed(seed) if seed else None)

    H = intH()
    W = intW()
    length = H * W
    permutation = Permutation(zero_indexed, seed=seed)
    generated = permutation(length=length)

    if not no_display_length:
        print(H, W)

    for i in range(H * W, step=W):
        print(*generated[i : i + W])
