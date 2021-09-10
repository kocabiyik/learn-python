def fib(n):
    """Returns n Fibonacci numbers with a recursive solution
    Args:
        n: number of Fibonacci numbers

    Returns:
        A list
    """

    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # recursive case
    else:
        return fib(n-1) + fib(n-2)

print([fib(x) for x in range(10)])
