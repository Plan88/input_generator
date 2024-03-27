from .generator import Generator


class String(Generator):
    def __init__(self, population: str, seed: int | None = None):
        super().__init__(seed)
        self.population = population

    def gen(self, length: int) -> str:
        """文字列を生成する

        Args:
            length (int): 文字列の長さ

        Returns:
            str: 長さlengthの文字列
        """
        return "".join(self.rand.choices(population=self.population, k=length))
