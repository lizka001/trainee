def lbinsearch(value, array):
    left = 0
    right = len(array) - 1
    while left < right:
        m = (left + right) // 2
        if array[m] < value:
            right = m
        else: left = m + 1
    return left

def rbinsearch(value, array):
    left = 0
    right = len(array) - 1
    while left < right:
        m = (left + right + 1) //2
        if array[m] > value:
            left = m
        else: right = m - 1
    return left


