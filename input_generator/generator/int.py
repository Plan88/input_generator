import math

from .generator import Generator


class Int(Generator):
    def __init__(
        self, low: int, high: int, log_scale: bool = False, seed: int | None = None
    ):
        super().__init__(seed)
        self.low = low
        self.high = high
        self.log_scale = log_scale

    def gen(self) -> int:
        """整数を生成する

        Returns:
            int: 整数
        """
        if self.log_scale:
            low = math.log2(self.low)
            high = math.log2(self.high)
            x = self.rand.random() * (high - low) + low
            x = int(2**x)
        else:
            x = self.rand.randint(self.low, self.high)
        return x
