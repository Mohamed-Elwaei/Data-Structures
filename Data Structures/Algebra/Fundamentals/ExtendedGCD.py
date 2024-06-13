
def gcd(a,b,x,y):
    if b==0:
        x[0],y[0]=1,0
        return a
    x1,y1=[0],[0]
    d=gcd(b,a%b,x1,y1)
    x[0]=y1[0]
    y[0]=(x1[0]-(a//b)*y1[0])
    return d
    
def extended_euclidean_algorithm(a, b):
    if b==0:
        return a,1,0  #GCD x1, y1
    
    gcd,x1,y1=extended_euclidean_algorithm(b,a%b)
    x=y1
    y=(x1-(a//b)*y1)
    return gcd,x,y



a = 48
b = 18
gcd, x, y = extended_euclidean_algorithm(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
