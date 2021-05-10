import argparse

parser = argparse.ArgumentParser(description="Factorial")
parser.add_argument("--n", type=int, default=0)
args = parser.parse_args()


def factorial(n):
    """Return n factorial

    Args:
        n: an integer
    """

    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(n=args.n))
