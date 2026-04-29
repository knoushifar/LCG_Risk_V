from lcg import lcg


def main() -> None:
    modulus = 17
    multiplier = 7
    increment = 3
    seed = 6
    count = 20

    generator = lcg(modulus, multiplier, increment, seed)

    print("Linear Congruential Generator Output:")
    print("-" * 40)

    for i in range(count):
        print(f"{i + 1:02d}: {next(generator)}")


if __name__ == "__main__":
    main()