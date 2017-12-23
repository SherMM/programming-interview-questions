import sys
import random


def bubble_sort(array):
    """
    docstring
    """

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    for _ in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
    


if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(151))
    print("original array: ")
    print(array)
    correct_answer = sorted(array)
    bubble_sort(array)
    print(array)
    print("sort is correct: {}".format(correct_answer == array))