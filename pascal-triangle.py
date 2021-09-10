from typing import List


def pascal_triangle(n: int = 5) -> List:
    """Returns nth row of Pascal Triangle

                 1
             1       1
         1       2       1
      1      3       3       1

    Args:
        n: An integer indicating the depth
    Return:
        A set

    >>> pascal_triangle(n=3)
    [[1], [1, 1], [1, 2, 1]]
    """

    triangle = [[1], [1, 1]]
    for i in range(3, n + 1):
        middle_series = []
        last_row = triangle[-1]
        for j in range(len(last_row) - 1):
            elem = last_row[j] + last_row[j + 1]
            middle_series.append(elem)
        new_row = [1] + middle_series + [1]
        triangle.append(new_row)
    return triangle


print(pascal_triangle(8))
