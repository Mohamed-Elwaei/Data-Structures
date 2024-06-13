from math import isqrt
def binpow(a,b,m):
    if b==0:
        return 1
    res=binpow(a,b//2,m)
    if b%2==1: #b is odd
        return res*res*a%m
    else:
        return res*res%m
    


def discrete_log(a, b, m):
    a%=m
    b%=m
    vals={}
    n=int(m**0.5)+1

    for p in range(1,n+1):
        vals[binpow(a,n*p,m)]=p
    
    for q in range(n+1):
        curr=binpow(a,q,m)*b
        if curr in vals:
            ans=vals[curr]*n - q
            return ans
    return -1 

print(discrete_log(2, 3, 5))
print(discrete_log(3, 5, 17))
print(discrete_log(4, 2, 13))
