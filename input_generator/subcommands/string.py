import enum
import string
from typing import List, Optional

import typer
from typing_extensions import Annotated

from ..generator.int import Int
from ..generator.string import String
from ..utils import next_seed

app = typer.Typer()


class CharType(str, enum.Enum):
    lower = "lower"
    upper = "upper"
    digit = "digit"


def _gen(
    population: str, min_len: int, max_len: int, seed: int | None
) -> tuple[int, string]:
    int_ = Int(low=min_len, high=max_len, seed=seed)
    length = int_()
    string_ = String(population=population, seed=seed)
    generated = string_(length)
    return length, generated


@app.command()
def line(
    min_len: int,
    max_len: int,
    char_type: Annotated[Optional[List[CharType]], typer.Option()] = [],
    additional_char: Annotated[Optional[str], typer.Option()] = "",
    no_display_length: Annotated[bool, typer.Option("--no-display-length")] = True,
    allow_leading_zero: Annotated[bool, typer.Option("--allow-leading-zero")] = False,
    seed: Optional[int] = None,
):
    population = ""
    for c in set(char_type):
        if c == CharType.lower:
            population += string.ascii_lowercase
        elif c == CharType.upper:
            population += string.ascii_uppercase
        elif c == CharType.digit:
            population += string.digits

    if additional_char:
        population += additional_char

    if not population:
        print("No population provided")
        raise typer.Abort()

    length, generated = _gen(population, min_len, max_len, seed)
    if not allow_leading_zero and generated[0] == "0":
        generated[0] = "1"

    if not no_display_length:
        print(length)
    print(generated)


@app.command()
def multilines(
    min_height: int,
    max_height: int,
    min_width: int,
    max_width: int,
    char_type: Annotated[Optional[List[CharType]], typer.Option()] = [],
    additional_char: Annotated[Optional[str], typer.Option()] = "",
    no_display_length: Annotated[bool, typer.Option("--no-display-length")] = False,
    allow_leading_zero: Annotated[bool, typer.Option("--allow-leading-zero")] = False,
    seed: Optional[int] = None,
):
    population = ""
    for c in set(char_type):
        if c == CharType.lower:
            population += string.ascii_lowercase
        elif c == CharType.upper:
            population += string.ascii_uppercase
        elif c == CharType.digit:
            population += string.digits

    if additional_char:
        population += additional_char

    if not population:
        print("No population provided")
        raise typer.Abort()

    intH = Int(min_height, max_height, seed=seed)
    intW = Int(min_width, max_width, seed=next_seed(seed) if seed else None)

    H = intH()
    W = intW()

    string_ = String(population, seed=seed)
    generated = "\n".join([string_(length=W) for _ in range(H)])

    if not no_display_length:
        print(H, W)
    print(generated)
