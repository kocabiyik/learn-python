# Given two sets A an B, return all the (a, b) combinations
# where a is an element of A and B is an element of B.

from typing import Set, List, Tuple
import itertools as it


def get_cartesian_product(A: Set, B: Set) -> List[Tuple]:
    """Returns Cartesian product of set A and B

    Args:
        A: A set
        B: A set
    Returns:
        List of Tuples in the form of (a, b)

    >>> get_cartesian_product(A={1, 2}, B={3, 4})
    [(1, 3), (1, 4), (2, 3), (2, 4)]

    """
    cartesian_product = []
    for a in A:
        for b in B:
            cartesian_product.append((a, b))
    return cartesian_product

def get_cartesian_product2(A: Set, B: Set) -> List[Tuple]:
    """Returns Cartesian product of set A and B

    Args:
        A: A set
        B: A set
    Returns:
        List of Tuples in the form of (a, b)
        
    >>> get_cartesian_product2(A={1, 2}, B={3, 4})
    [(1, 3), (1, 4), (2, 3), (2, 4)]
    """

    return list(it.product(A, B))

