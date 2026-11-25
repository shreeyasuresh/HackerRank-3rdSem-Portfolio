"""Count how often each query string appears in a list of strings."""


def matchingStrings(stringList, queries):
    """Return the frequency of each query in stringList."""
    frequencies = {}

    for item in stringList:
        frequencies[item] = frequencies.get(item, 0) + 1

    return [frequencies.get(query, 0) for query in queries]


if __name__ == "__main__":
    import sys

    input_values = sys.stdin.buffer.read().decode().split()
    string_count = int(input_values[0])
    strings = input_values[1:1 + string_count]

    query_count_index = 1 + string_count
    query_count = int(input_values[query_count_index])
    queries = input_values[query_count_index + 1:query_count_index + 1 + query_count]

    print("\n".join(map(str, matchingStrings(strings, queries))))
