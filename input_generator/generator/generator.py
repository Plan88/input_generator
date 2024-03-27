import random
from abc import ABCMeta, abstractmethod


class Generator(metaclass=ABCMeta):
    def __init__(self, seed: int | None = None):
        self.rand = random.Random(seed)

    @abstractmethod
    def gen(self):
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        return self.gen(*args, **kwargs)
