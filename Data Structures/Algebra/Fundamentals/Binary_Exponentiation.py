def binpow(a, b):

    if b==0:
        return 1
    res=binpow(a,b//2)

    if b%2==1:
        return res*res*a
    else:
        return res*res

def binpow(a,b):
    res=1
    while b>0:
        if b%2:
            res*=a
        a*=a
        b//=2
    return res
print(binpow(3,4) == 3**4)


