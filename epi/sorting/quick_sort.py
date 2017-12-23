import sys
import random 


def quicksort(array):
    """
    docstring
    """
    if len(array) <= 1:
        return array
    pivot = random.choice(array)
    lt, eq, gt = partition(array, pivot)
    return quicksort(lt) + eq + quicksort(gt)

def partition(array, pivot):
    lt, eq, gt = [], [], []
    for val in array:
        if val < pivot:
            lt.append(val)
        elif val == pivot:
            eq.append(val)
        else:
            gt.append(val)
    return lt, eq, gt


if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(151))
    print("original array")
    print(array)
    correct_answer = sorted(array)
    s = quicksort(array)
    print(s)
    print("sort is correct: {}".format(s == correct_answer))