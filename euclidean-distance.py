import math


def calculate_distance(p1, p2):
    """
    Calculates distance between two points on the Cartesian space.

    Args:
        p1: A tuple containing (x, y) coordinates
        p2: A tuple containing (x, y) coordinates

    Returns:
        The Euclidian distance between p1 and p1. A float.

    >>> calculate_distance(p1=(1,1), p2 = (4, 5))
    5.0
    >>> calculate_distance(p1=(1,0), p2 = (0, 0))
    1.0

    """

    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def find_closest_points(points):
    """Returns closest two points from an array.

    Args:
        points: List of (x, y) tuples.
    Returns:
        A list of containing two tuples.
    """

    dist_matrix = []
    for p_chosen in points:
        dist = []
        for p in points:
            distance = calculate_distance(p_chosen, p)
            dist.append(distance)

        dist_matrix.append(dist)

    measures = {}
    pairs = []

    for i, row in enumerate(dist_matrix):
        row_non_zero = [d for d in row if d != 0.0]
        min_distance = min(row_non_zero)

        closest_point = row.index(min_distance)
        pair = (i, closest_point)

        pairs.append(pair)

        measures[pair] = min_distance

        ranked = sorted(measures.items(), key=lambda item: item[1])

    selected_point1 = points[ranked[0][0][0]]
    selected_point2 = points[ranked[0][0][1]]
    return selected_point1, selected_point2


# list of tuples containing coordinates
test_points = [(9, 0), (1, 0), (3, 5)]

print(find_closest_points(test_points))
