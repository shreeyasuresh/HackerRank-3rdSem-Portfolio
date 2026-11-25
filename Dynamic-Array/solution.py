"""Process queries over a collection of dynamically selected sequences."""


def dynamicArray(n, queries):
    """Return the answers produced by all type-2 queries."""
    sequences = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query_type, x, y in queries:
        sequence_index = (x ^ lastAnswer) % n

        if query_type == 1:
            sequences[sequence_index].append(y)
        else:
            sequence = sequences[sequence_index]
            lastAnswer = sequence[y % len(sequence)]
            answers.append(lastAnswer)

    return answers


if __name__ == "__main__":
    import sys

    input_values = list(map(int, sys.stdin.buffer.read().split()))
    sequence_count = input_values[0]
    query_count = input_values[1]
    queries = []

    for query_index in range(query_count):
        start = 2 + query_index * 3
        queries.append(input_values[start:start + 3])

    print("\n".join(map(str, dynamicArray(sequence_count, queries))))
