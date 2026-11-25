"""Compare Alice's and Bob's three scores."""


def compareTriplets(a, b):
    """Return the points earned by Alice and Bob, in that order."""
    alice_score = 0
    bob_score = 0

    for alice_value, bob_value in zip(a, b):
        if alice_value > bob_value:
            alice_score += 1
        elif bob_value > alice_value:
            bob_score += 1

    return [alice_score, bob_score]


if __name__ == "__main__":
    import sys

    alice_scores = list(map(int, sys.stdin.buffer.readline().split()))
    bob_scores = list(map(int, sys.stdin.buffer.readline().split()))

    print(*compareTriplets(alice_scores, bob_scores))
