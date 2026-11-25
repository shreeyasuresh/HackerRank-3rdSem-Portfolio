"""Calculate the absolute difference between a square matrix's diagonals."""


def diagonalDifference(arr):
    """Return the absolute difference between the two diagonal sums."""
    matrix_size = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for index in range(matrix_size):
        primary_sum += arr[index][index]
        secondary_sum += arr[index][matrix_size - 1 - index]

    return abs(primary_sum - secondary_sum)


if __name__ == "__main__":
    import sys

    input_values = list(map(int, sys.stdin.buffer.read().split()))
    matrix_size = input_values[0]
    matrix = []

    for row_index in range(matrix_size):
        start = 1 + row_index * matrix_size
        matrix.append(input_values[start:start + matrix_size])

    print(diagonalDifference(matrix))
