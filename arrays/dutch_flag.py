import sys
import random
import itertools


def group_integers_inplace(numbers, pidx):
    """
    Groups (inplace) numbers by less-than-numbers[pidx],
    equal-to-numbers[pidx], and greater-than-numbers[pidx]

    Args:
        numbers (list[int]): list of integers
        pidx (int): index of pivot
    
    Returns:
        N/A
    """
    def swap(array, i, j):
        array[i], array[j] = array[j], array[i]

    pivot = numbers[pidx]
    low = 0
    # group integers that are less than the pivot
    for i in range(len(numbers)):
        if numbers[i] < pivot:
            swap(numbers, i, low)
            low += 1

    high = len(numbers) - 1
    # group integers that are greater than the pivot
    for i in range(high, low-1, -1):
        if numbers[i] > pivot:
            swap(numbers, i, high)
            high -= 1


def group_integers(numbers, pivot):
    """
    Returns a list where numbers are ordered
    by less-than-pivot, equal-to-pivot, and 
    greater-than-pivot.

    Args:
        numbers (list[int]): list of integers
        pivot (int): integer to order/group integers by

    Returns:
        ordered (list[int]): new list where numbers are
            ordered according to constraints listed in the 
            docstring
    """
    lt, eq, gt = [], [], []
    for number in numbers:
        if number < pivot:
            lt.append(number)
        elif number == pivot:
            eq.append(number)
        else:
            gt.append(number)
    return list(itertools.chain(lt, eq, gt))


def get_pivot_lo_hi_index(numbers, pivot):
    """
    Returns index of first and last pivot 
    occurrence 

    Args:
        numbers (list[int]): list of integers
        pivot (int): pivot value

    Returns:
        (lo, hi): indices of first and last
            pivot value occurrences
    """
    lo, hi = None, None
    for i, value in enumerate(numbers):
        if value == pivot:
            if lo is None:
                lo, hi = i, i
            else:
                hi += 1
    return lo, hi


def all_pivots_contiguous(numbers, pivot):
    """
    Returns true if all pivot values are in a contiguous 
    block in the list

    Args:
        numbers (list[int]): list of integers
        pivot (int): pivot value
    
    Returns:
        bool: True/False if block of 
            pivot values is/is-not conitguous
    """
    lo, hi = get_pivot_lo_hi_index(numbers, pivot)
    return all(v == pivot for v in numbers[lo: hi+1])


def all_numbers_grouped_around_pivot(numbers, pivot):
    """
    Returns true if all values less than the pivot 
    appear before the pivot in the array and all values
    greater than the pivot appear after the pivot in the 
    array

    Args:
        numbers (list[int]): list of integers
        pivot (int): pivot value 
        lo (int): index in ordered list where first
            occurrence of pivot appears
        hi (int): index in ordered list where last
            occurrence of pivot appears
    """
    lo, hi = get_pivot_lo_hi_index(numbers, pivot)
    lower = all(v < pivot for v in numbers[:lo])
    higher = all(v > pivot for v in numbers[hi+1:])
    return lower and higher


if __name__ == "__main__":
    size = int(sys.argv[1])
    lo, hi = 0, 25
    numbers = [random.randrange(lo, hi) for _ in range(size)]
    pidx = random.randrange(0, len(numbers))
    pivot = numbers[pidx]
    print("Original List:")
    print(numbers)
    print("Pivot: {}".format(pivot))
    print()
    print("Ordered List:")
    new_numbers = group_integers(numbers, pivot)
    print(group_integers(numbers, pivot))
    print()

    assert all_pivots_contiguous(new_numbers, pivot) == True
    assert all_numbers_grouped_around_pivot(new_numbers, pivot) == True
    print("All Test Cases Passed!")
    print()

    print("Original List:")
    print(numbers)
    print("Pivot: {}".format(pivot))
    print()
    print("Ordered List:")
    group_integers_inplace(numbers, pidx)
    print(numbers)
    print()

    assert all_pivots_contiguous(numbers, pivot) == True
    assert all_numbers_grouped_around_pivot(numbers, pivot) == True
    print("All Test Cases Passed!")
    

