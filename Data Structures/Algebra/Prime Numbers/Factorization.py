def trial_division(n):
    factorization = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        factorization.append(n)
    return factorization


print(trial_division(14))

import math

import math

def fermat_factorization(n):
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    b = round(math.sqrt(b2))
    
    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = round(math.sqrt(b2))
    
    return a - b,a+b



def fermat_factorization(n):
    a=math.ceil(math.sqrt(n))
    b2=a*a-n
    b=int(math.sqrt(b2))

    while b*b!=b2:
        a+=1
        b2=a*a-n
        b=math.isqrt(b2)
    return a-b,a+b




# Example usage
composite_number = 8051
result = fermat_factorization(composite_number)
print("Factor:", result)

