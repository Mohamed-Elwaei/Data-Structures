def factmod(n, p):
    f = [0] * p
    f[0] = 1

    for i in range(1, p):
        f[i] = (f[i - 1] * i) % p

    res = 1

    while n > 1:
        if (n // p) % 2:
            res = p - res
        res = (res * f[n % p]) % p
        n //= p

    return res




print(factmod(7, 3))