import argparse

parser = argparse.ArgumentParser(
    description="Prints Fibonacci numbers up to a limit")
parser.add_argument("--up_to", type=int, default=100,
                    help="The upper limit for the Fibonacci sequence")
args = parser.parse_args()


def fibonacci_sequence(up_to=100):
    """
    Returns fibonacci numbers up to the given limit.

    Args:
        up_to (int): the upper limit of the fibonacci series

    Returns:
       A list of fibonacci numbers
    """

    seq = [0, 1]
    while seq[-1] < up_to:
        fib_next = seq[-1] + seq[-2]
        seq.append(fib_next)

    if seq[-1] > up_to:
        seq.remove(fib_next)

    print(seq)


fibonacci_sequence(args.up_to)
