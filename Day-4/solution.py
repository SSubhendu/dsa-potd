def modulo(s, m):
    k = 0
    for c in s:
        k = k * 2 + int(c)
    return k % m
