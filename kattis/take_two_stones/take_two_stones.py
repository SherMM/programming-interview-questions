import sys


def first_to_play_wins(stones):
    """
    docstring
    """
    return stones % 2


def get_winning_player(stones):
    if first_to_play_wins(stones):
        return "Alice"
    return "Bob"


if __name__ == "__main__":
    stones = int(sys.stdin.readline())
    print(get_winning_player(stones))
    
