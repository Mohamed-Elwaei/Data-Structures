import numpy as np
def Insertion_Sort(arr):
    if len(arr)<2:
        return
    
    for i in range(1,len(arr)):
       key=arr[i]
       j=i-1
       while j>-1 and arr[j]>key:
           arr[j+1]=arr[j]
           j-=1
       arr[j+1]=key
       
       
arr=[x for x in range(10,-1,-1)]
Insertion_Sort(arr)
print(arr)