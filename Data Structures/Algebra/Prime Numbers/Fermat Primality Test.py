import random

def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        print(a, pow(a, n - 1, n))
        if pow(a, n - 1, n) != 1:
            return False
    return True


def is_prime(n, k=6):
    if n==2 or n==3:
        return True
    if n%2==0 or n<=1:
        return False
    
    for _ in range(k):
        a=random.randint(2,n-2)
        if pow(a,n-1,n)!=1:
            return False
    return True



t=int(input())

for _ in range(t):
    i=int(input())
    if is_prime(i):
        print('YES')
    else:
        print("NO")