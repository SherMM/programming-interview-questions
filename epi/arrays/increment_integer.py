import sys
import random
from collections import deque


def increment_integer(integer):
    """
    docstring
    """
    number = deque()
    carry = 1
    for i in range(len(integer)-1, -1, -1):
        number.appendleft((integer[i] + carry) % 10)
        carry = (integer[i] + carry) // 10
    if number[0] == 0:
        number.appendleft(1)
    return number


def convert_number_array_to_string(number):
    return "".join(str(v) for v in number)


if __name__ == "__main__":
    n = int(sys.argv[1])
    integer = [random.randrange(1, 10)]
    for _ in range(n):
        integer.append(random.randrange(10))
    
    print(convert_number_array_to_string(integer))
    number = increment_integer(integer)
    print(convert_number_array_to_string(number))