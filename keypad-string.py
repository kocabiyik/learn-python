def get_mapping():
    import string
    possible_digits = string.digits
    possible_characters = string.ascii_lowercase

    mapping = {}
    start_index = 0
    for d in possible_digits:
        if d == '0':
            mapping[d] = " "
        elif d == '1':
            mapping[d] = ""
        else:
            if d in {'7', '9'}:
                str_len = 4
            else:
                str_len = 3
            mapping[d] = possible_characters[start_index:start_index + str_len]
            start_index += str_len
    return mapping


def keypad_string(keys: str) -> str:
    """
    Given a string consisting of 0-9, find the string that is created using a standard phone keyboard.
    -------------------------
    |       |  ABC  |  DEF  |
    |   1   |   2   |   3   |
    -------------------------
    |  GHI  |  JKL  |  MNO  |
    |   4   |   5   |   6   |
    -------------------------
    | PQRS  |  TUV  | WXYZ  |
    |   7   |   8   |   9   |
    -------------------------
    |       |       |       |
    |   *   |   0   |   #   |
    -------------------------

    >>> keypad_string('12345')
    'adgj'

    Returns:
        A string
    """
    return get_mapping()


print(keypad_string('90789'))
