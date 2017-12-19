import sys


def perform_spell(n):
    """
    docstring
    """
    for i in range(n):
        print("{} Abracadabra".format(i+1))


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    perform_spell(n)