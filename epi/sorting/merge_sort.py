import sys
import random 


def mergesort(array):
    """
    docstring
    """
    if len(array) <= 1:
        return array
    left, right = split(array)
    return merge(mergesort(left), mergesort(right))


def merge(arr1, arr2):
    """
    docstring
    """
    i, j = 0, 0
    array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            array.append(arr1[i])
            i += 1
        else:
            array.append(arr2[j])
            j += 1
    array.extend(arr1[i:])
    array.extend(arr2[j:])
    return array


def split(array):
    m = len(array) // 2
    return array[:m], array[m:]


if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(151))
    print("original array")
    print(array)
    correct_answer = sorted(array)
    s = mergesort(array)
    print(s)
    print("sort is correct: {}".format(s == correct_answer))