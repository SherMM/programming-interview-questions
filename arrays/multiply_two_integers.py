import sys

def to_integer_array(string):
    """
    docstring
    """
    return [int(v) for v in list(string)]


def multiply(num1, num2):
    """
    docstring
    """
    # make sure smaller number (less digits)
    # is iterated in outer loop to mimic
    # normal multiplication process
    for digit1 in reversed(num2):
        for digit2 in num1:
            print("{} X {} = {}".format(digit1, digit2, digit1*digit2))


if __name__ == "__main__":
    num1, num2 = sys.argv[1:]
    num1 = to_integer_array(num1)
    num2 = to_integer_array(num2)
    print(num1)
    print(num2)
    multiply(num1, num2)