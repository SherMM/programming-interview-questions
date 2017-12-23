import sys
import random


def selection_sort(array):
    """
    docstring
    """
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(len(array)):
        min_value = array[i]
        min_index = i
        for j in range(i+1, len(array)):
            value = array[j]
            if value < min_value:
                min_value = value
                min_index = j
        swap(array, i, min_index)
    

if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(151))

    print("orginal array")
    print(array)
    correct_answer = sorted(array)
    selection_sort(array)
    print()
    print()
    print("sorted array")
    print(array)
    print("sort is correct: {}".format(correct_answer == array))