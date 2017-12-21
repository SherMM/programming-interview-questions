import sys
import random

def remove_duplicates(array):
    """
    docstring
    """
    arr = []
    seen = set()
    for value in array:
        if value not in seen:
            arr.append(value)
            seen.add(value)
    return arr


def remove_duplicates_inplace(array):
    """
    docstring
    """
    # first position in array is first 
    # unique element
    curr = array[0]
    # index is position in array to move
    # unique element to and length will be 
    # size of new, uniques-only array
    index, length = 1, 1
    for i in range(1, len(array)):
        if array[i] != curr:
            array[index] = array[i]
            curr = array[i]
            index += 1
            length += 1
    return array[:length]
        


if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(25))
    array.sort()
    print(array)
    no_dups = remove_duplicates_inplace(array)
    print(no_dups)