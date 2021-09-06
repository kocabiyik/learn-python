from typing import List


def rotate_image(img: List) -> List:
    """Rotates an image
    >>> rotate_image([[1,2,3],[4,5,6],[7,8,9]])
    [[7,4,1],[8,5,2],[9,6,3]]
    """

    # 1. transpose
    # 2. reverse

    matrix_transposed = [[0, 0, 0] for _ in range(3)]
    for i in range(3):  # <--  O(n**2)
        for j in range(3):
            matrix_transposed[j][i] = img[i][j]
    return matrix_transposed


print(rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
