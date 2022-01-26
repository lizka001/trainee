def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) //2
        if check(m , params):
            r = m
        else:
            l = m + 1
    return l

def check(m, params):
    n, k = params
    return 2 * n <= (2 * k + m - 1) * m

n = 300
k = 40

print(lbinsearch(0, n, check, [n, k]))

