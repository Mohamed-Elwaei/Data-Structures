def sieve(n):
    if n<=2:
        return 0

    primes=[True]*n
    primes[0]=primes[1]=False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j]=False
    return sum(primes)
 

def linear_sieve(limit):
    lowest_prime_factor = [0] * (limit+1)
    primes = []

    for number in range(2, limit+1):
        if lowest_prime_factor[number] == 0:
            # number is prime
            lowest_prime_factor[number] = number
            primes.append(number)

        index = 0
        while index < len(primes) and number * primes[index] <= limit:
            multiple = number * primes[index]
            lowest_prime_factor[multiple] = primes[index]

            if primes[index] == lowest_prime_factor[number]:
                # Break if the lowest prime factor of the multiple is equal to the current prime
                break

            index += 1
    return primes

# def linear_sieve(N):
#     lp = [0] * (N+1)
#     pr = []

#     for i in range(2, N+1):
#         if lp[i] == 0:
#             lp[i] = i
#             pr.append(i)
#         j = 0
#         while i * pr[j] <= N:
#             lp[i * pr[j]] = pr[j]
#             if pr[j] == lp[i]:
#                 break
#             j += 1



def linear_sieve(n):
    primes=[]
    lp=[0]*(n+1)

    for i in range(2,n+1):
        if lp[i]==0:
            primes.append(i)
            lp[i]=i

        j=0
        while i*primes[j]<=n+1:
            lp[i*primes[j]]=primes[j]

            if lp[i]==primes[j]:
                break
            j+=1
    return primes


def linear_sieve(limit):
    primes=[]
    lp=[0]*(limit+1)

    for num in range(2,limit):

        if lp[num]==0:
            lp[num]=num
            primes.append(num)
        
        idx=0
        while num*primes[idx]<=limit:
            lp[num*primes[idx]]=primes[idx]
            if primes[idx]==lp[num]: 
                break

            idx+=1
    return primes


print(sieve(10))