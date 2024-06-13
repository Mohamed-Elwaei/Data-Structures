


def EEA(a,m):

    if m==0:
        return a,1,0 #GCD,x1,y1
    
    GCD,x1,y1,=EEA(m,a%m)
    x=y1
    y=x1-(a//m)*y1

    return GCD,x,y





def inv(a,m):
    
    GCD,x,y=EEA(a,m)

    if GCD==1:
        return x
    return -1



def CRT(congruences):
    #[ai, mi]

    M=1
    for ai,mi in congruences:
        M*=mi

    a=0 #Solution
    for ai,mi in congruences:
        Mi=M/mi
        Ni=inv(Mi,mi)
        a+=(Mi*ai*Ni)

    return a%M
        

        
result = inv(3, 11)
print(result)  # Expected output: 4 (because 3 * 4 % 11 = 1)

result = inv(7, 26)
print(result)  # Expected output: 15 (because 7 * 15 % 26 = 1)

result = inv(8, 12)
print(result)  # Expected output: -1 (no modular inverse exists)

result = inv(17, 31)
print(result)  # Expected output: 22 (because 17 * 22 % 31 = 1)
