def gcd(a,b):
    if (b==0):
        return a
    return gcd(b,a%b)

# def gcd(a,b):
#     ans=b if b==0 else gcd(b,a%b)

# def gcd(a,b):

#     while b:
#         a,b=b,a%b
#     return a


def lcm(a,b):
    return (abs(a)*abs(b))/(gcd(a,b))


print(gcd(15,22))
print(gcd(24,36))
print(gcd(45,15))
print(gcd(17,51))
