"""
program that prints a sequence from the start to the end
"""
import argparse


def sequence_str(mini: int, maxi: int) -> str:
    """
    print sequence from the min to max value
    """
    return " ".join(str(num) for num in range(mini, maxi + 1))

def main(mini: int, maxi: int) -> None:
    """
    main entrypoint
    """
    print(sequence_str(mini, maxi))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('min', type=int)
    PARSER.add_argument('max', type=int)
    ARGS = PARSER.parse_args()
    MIN, MAX = ARGS.min, ARGS.max
    main(MIN, MAX)

