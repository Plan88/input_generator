from .generator import Generator


class Permutation(Generator):
    def __init__(self, is_0_indexed: bool = False, seed: int | None = None):
        super().__init__(seed)
        self.is_0_indexed = is_0_indexed

    def gen(self, length: int) -> list[int]:
        """順列を生成する

        Args:
            length (int): 順列の長さ
            is_0_indexed (bool): 0-indexedかどうか, defaults False

        Returns:
            list[int]: 長さlengthの順列
        """
        base = 0 if self.is_0_indexed else 1
        p = list(range(base, length + base))
        self.rand.shuffle(p)
        return p
