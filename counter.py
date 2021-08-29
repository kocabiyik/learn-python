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
