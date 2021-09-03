from collections import Counter


def get_top_three_letters(string):
    """
    Get top 3 frequent letters and their counts.
    Args:
        string:

    Returns:
        A set of tuples with letter count pairs
    """
    string_list = list(string.upper())

    records = {}
    for s in string_list:
        if s in records.keys():
            records[s] += 1
        else:
            records[s] = 1

    records = sorted(records.items(), key=lambda item: item[1], reverse=True)

    return records[0:3]


print(get_top_three_letters("Imran Kocabiyik"))


def count_letters(string):
    """
    Counts letters of a string excluding spaces.
    Args:
        string: A string

    Returns:
        Visual representation of the count. A string.
    """

    string_list = list(string.replace(" ", "").upper())
    string_counts = Counter(string_list)
    letter_count_ordered = string_counts.most_common()

    for c in letter_count_ordered:
        print(c[0], ':', '+' * c[1])

    return letter_count_ordered


print(count_letters("Lorem ipsum sit dolor amet."))
