import numpy as np

def counting_sort(A):
    #O(n+k)
    Max, Min=max(A), min(A)
    Range=Max-Min+1
    count=[0] *Range
    
    for i in A:
        count[i-Min]+=1
        
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    
    output=[0]*len(A)
    for i in A:
        output[count[i-Min]-1]=i
        count[i-Min]-=1
    return output
    

for _ in range(10):
    A=[10,7,9,5,6,3,4,1,2]
    print(counting_sort(A) == sorted(A))