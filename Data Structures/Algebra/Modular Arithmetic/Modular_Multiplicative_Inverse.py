def EEA(a,b):
    if b==0:
        return a,1,0 #GCD,x1,y1
    GCD,x1,y1=EEA(b,a%b)
    x=y1
    y=(x1-(a//b)*y1)

    return GCD,x,y





def modular_multiplicative_inverse(a, m):
    gcd, x, y = EEA(a, m)
    if gcd != 1:
        # Modular multiplicative inverse doesn't exist
        return None
    else:
        # Ensure the result is positive
        return x%m



def inv(i, m):
    if i <= 1:
        return i
    else:
        return m - (m // i) * inv(m % i, m) % m


a = 7
m = 26
result = modular_multiplicative_inverse(30,7)
print(result)


