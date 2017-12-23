import sys
import random


def insertion_sort(array):
    """
    docstring
    """
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(array, j, j-1)
            j -= 1
    

if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(151))

    print("orginal array")
    print(array)
    correct_answer = sorted(array)
    insertion_sort(array)
    print("sorted array")
    print(array)
    print("sort is correct: {}".format(correct_answer == array))