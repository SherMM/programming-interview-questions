import sys
import random


def can_advance_to_end(board):
    """
    docstring
    """
    furthest = 0
    i = 0
    while i <= furthest and furthest < len(board)-1:
        furthest = max(furthest, i + board[i])
        i += 1
    return furthest >= len(board)-1


if __name__ == "__main__":
    n = int(sys.argv[1])
    board = []
    for _ in range(n):
        board.append(random.randrange(5))
    print(board)
    print(can_advance_to_end(board))