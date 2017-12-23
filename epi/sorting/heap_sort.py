import sys
import random
import heapq


def heapsort(array):
    heap = []
    for value in array:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for _ in range(len(heap))]


if __name__ == "__main__":
    n = int(sys.argv[1])
    array = []
    for _ in range(n):
        array.append(random.randrange(151))
    
    print("original array")
    print(array)
    correct_answer = sorted(array)
    s = heapsort(array)
    print(s)
    print("sort is correct: {}".format(s == correct_answer))