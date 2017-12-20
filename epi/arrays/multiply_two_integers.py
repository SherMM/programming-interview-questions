import sys
from collections import deque

def to_integer_array(string):
    """
    docstring
    """
    return [int(v) for v in list(string)]


def integer_array_to_string(integer):
    """
    docstring
    """
    if len(integer) == 0:
        return "0"
    return "".join(str(v) for v in integer)


def multiply(num1, num2):
    """
    docstring
    """
    # make sure smaller number (less digits)
    # is iterated in outer loop to mimic
    # normal multiplication process
    integer = deque([0]*(len(num1) + len(num2)))
    for i in range(len(num2)-1, -1, -1):
        for j in range(len(num1)-1, -1, -1):
            dig1, dig2 = num2[i], num1[j]
            integer[i+j+1] += (dig1 * dig2)
            integer[i+j] += integer[i+j+1] // 10
            integer[i+j+1] = integer[i+j+1] % 10

    # make sure there are now leading zeros
    index = 0
    while index < len(integer):
        if integer[index] != 0:
            break
        else:
            integer.popleft()
    return integer



if __name__ == "__main__":
    num1, num2 = sys.argv[1:]
    int1, int2 = int(num1), int(num2)
    print("Number 1: {}".format(num1))
    print("Number 2: {}".format(num2))
    print("Actual product: {}".format(int1 * int2))
    num1 = to_integer_array(num1)
    num2 = to_integer_array(num2)
    print()
    print("Product after list multiplication")
    print(integer_array_to_string(multiply(num1, num2)))