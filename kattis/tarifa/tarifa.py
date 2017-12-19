import sys

def calculate_rollover(mb_limit, usage):
    """
    docstring
    """
    rollover = 0
    for use in usage:
        rollover += (mb_limit - use)
    return rollover + mb_limit
    


if __name__ == "__main__":
    vals = []
    for val in sys.stdin:
        vals.append(int(val))

    mb_limit, _, *usage = vals
    print(calculate_rollover(mb_limit, usage))