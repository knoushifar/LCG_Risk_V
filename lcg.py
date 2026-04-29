from collections.abc import Generator


def lcg(modulus: int, multiplier: int, increment: int, seed: int) -> Generator[int, None, None]:
    """
    Generate pseudo-random numbers using a Linear Congruential Generator.

    Formula:
        X(n+1) = (a * X(n) + c) mod m
    """
    if modulus <= 0:
        raise ValueError("Modulus must be positive.")

    x = seed
    while True:
        x = (multiplier * x + increment) % modulus
        yield x