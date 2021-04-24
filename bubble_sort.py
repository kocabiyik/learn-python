import argparse

parser = argparse.ArgumentParser(description='Sorting numbers')
parser.add_argument('integers', nargs='+', type=float)


def bubble_sort(a_list):
    """
    Sorting a list with bubble method

    Args:
        a_list (list): A list of real numbers

    Returns:
        A list of floats
    """
    sorting_completed = False
    while not sorting_completed:
        for i in range(1, len(a_list)):
            if a_list[i-1] > a_list[i]:
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
                sorting_completed = all(
                    [a_list[i-1] < a_list[i] for i in range(1, len(a_list))])
    print(a_list)


args = parser.parse_args()
bubble_sort(args.integers)
