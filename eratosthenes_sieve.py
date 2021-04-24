import argparse

parser = argparse.ArgumentParser(
    description="Prints prime numbers up to a given limit")
parser.add_argument("--up_to", type=int, default=100,
                    help="The upper limit for the prime number.")
args = parser.parse_args()


def eratosthenes_sieve(upper_limit):
    """
    Returns prime numbers up to a given limit.

    Args:
        upper_limit (int): The upper limit

    Returns:
        A list of prime numbers
    """

    sieve = [n for n in range(2, upper_limit)]
    primes = []

    while len(sieve) != 0:
        prime_selected = sieve[0]
        sieve = [n for n in sieve if n % prime_selected != 0]
        primes.append(prime_selected)

    print(primes)


eratosthenes_sieve(args.up_to)
