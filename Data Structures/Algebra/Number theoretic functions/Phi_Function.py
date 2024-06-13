#Euler Phi
def phi(n):
    result = n
    i = 2
    while i * i <= n:
 
        while n % i == 0:
            n //= i
        result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result




def phi_1_to_n(n):
    phi = [i for i in range(n + 1)]
    
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi
    


for i in range(10,20):
    print(f"ø({i})",phi(i))