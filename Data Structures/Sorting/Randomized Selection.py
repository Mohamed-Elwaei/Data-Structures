import random
import numpy as np



def randomized_select(A,p,r,i):
    if p==r:
        return A[p]
    pivot=randomized_partition(A,p,r)
    k=pivot-p+1 #Number of elements less than or equal the pivot
    
    if k==i:    #if the Number of elements less than or equal the pivot is the same as the ith order stastic then the pivot is the answer
        return A[pivot]
    elif i<k:
        return randomized_select(A,p,pivot-1,i)
    elif i>k:
        return randomized_select(A,pivot+1,r,i-k)

def randomized_partition(A,p,r):
    num=random.randint(p,r)
    A[r],A[num]=A[num],A[r]
    return partition(A,p,r)


def partition(A,p,r):
    pivot=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
    
    

arr = np.random.randint(1,20,10)
k = 3
print(arr)
result = randomized_select(arr, 0, len(arr) - 1, k)
print(f"The {k}th smallest element is: {result}")
