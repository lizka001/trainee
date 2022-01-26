arr = [1, 5, 10, 15, 20, 22, 33, 40, 55, 67, 89, 100]


def binary_search(elem, arr):
    start_index = 0
    last_index = len(arr) - 1
    while start_index <= last_index:
        middle = (start_index + last_index) // 2
        guess = arr[middle]
        if guess == elem:
            return middle
        if guess < elem:
            start_index = middle + 1
        else:
            last_index = middle - 1
    return None


assert binary_search(10, arr) == 2
assert binary_search(100, arr) == 11
assert binary_search(1, arr) == 0
assert binary_search(4, arr) is None

print("Success")