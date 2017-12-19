import sys


def get_hour_glasses(array, l=3, h=3):
    """
    docstring
    """
    rows, cols = len(array), len(array[0])
    hour_glasses = []
    for i in range(rows - h+1):
        for j in range(cols - l+1):
            hg = []
            top = array[i][j: j+l]
            bottom = array[i+h-1][j: j+l]
            middle = array[i+1][j+1]
            hg.extend(top)
            hg.extend(bottom)
            hg.append(middle)
            hour_glasses.append(hg)
    return hour_glasses


def calculate_hour_glass_sum(hg):
    """
    docstring
    """
    return sum(hg)


def find_max_hour_glass_sum(array):
    """
    pass
    """
    max_hg = float("-inf")
    for hg in get_hour_glasses(array):
        hg_sum = calculate_hour_glass_sum(hg)
        if hg_sum > max_hg:
            max_hg = hg_sum
    return max_hg



if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    array = []
    for line in lines:
        l = [int(v) for v in line.split()]
        array.append(l)

    print(find_max_hour_glass_sum(array))