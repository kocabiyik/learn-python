def reverse_integer(x: int) -> int:
    """
    Reverses digits of an integer
    >>> reverse_integer(123)
    321
    >>> reverse_integer(287)
    782
    """
    is_negative = True if x < 0 else False
    x = abs(x)
    string_repr = str(x)
    string_repr_reversed = list(reversed(string_repr))
    string_reversed = ''.join(string_repr_reversed)
    x_reversed = int(string_reversed)
    x_corrected = (-1)*x_reversed if is_negative else x_reversed
    return x_corrected

print(reverse_integer(-234))
