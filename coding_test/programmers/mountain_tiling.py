def solution(n, tops):
    mod = 10_007
    a = [0] * n
    b = [0] * n
    a[0] = 1
    b[0] = 2 + tops[0]
    for i in range(1, n):
        a[i] = (a[i - 1] + b[i - 1]) % mod
        b[i] = ((a[i - 1] * (1 + tops[i])) + (b[i - 1] * (2 + tops[i]))) % mod
    return (a[-1] + b[-1]) % mod
