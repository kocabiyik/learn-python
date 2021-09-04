from itertools import combinations
from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Returns tuple in which the sum of the items equal to target.
    Args:
        nums: list of integers
        target: target integer

    Returns:
        A tuple from the nums list


    >>> two_sum([1, 2, 8], 3)
    (0, 1)

    >>> two_sum([3, 4, 7, 9, 1], 16)
    (2, 3)
    """

    combs = list(combinations(nums, r=2))
    picked = [c for c in combs if c[0] + c[1] == target][0]
    first = picked[0]
    second = picked[1]
    first_index = nums.index(first)
    nums[first_index] = "_"
    second_index = nums.index(second)
    return first_index, second_index

print(two_sum([3, 3], 6))