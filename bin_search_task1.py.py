def lbinarysearch(left, right, check, params):
    while left <  right:
        m = (left + right) // 2
        if check(m, params):
            right = m
        else:
            left = m + 1
    return left

def checkfuction(m , param):
    n , k = param
    return (k + m) * 3 >= n + m

n = 100
k = 10
print(lbinarysearch(0, n, checkfuction, [n, k]))

