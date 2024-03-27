A = 1_103_515_245
B = 12_345
M = 2_147_483_647


def next_seed(seed: int) -> int:
    global A, B, M
    return (A * seed + B) % M
