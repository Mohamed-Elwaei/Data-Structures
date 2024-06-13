import numpy as np

# Function to compute the nth Fibonacci number using matrix multiplication
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    matrix = np.array([[1,1],[1,0]])
    matrix=binpow(matrix, n-1)

    return matrix[0][0]

def binpow(matrix, n):

    if n==0:
        return np.array([[1,0],[0,1]])
    
    result = binpow(matrix, n//2)

    if n%2:
        return result@result@matrix
    else:
        return result@result

# Test the algorithm
n = 10
fibonacci_number = fibonacci(10)

for i in range()
print(f"The {n}th Fibonacci number is: {fibonacci_number}")
