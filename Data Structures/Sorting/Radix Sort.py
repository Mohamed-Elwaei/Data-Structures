import numpy as np
def counting_sort(arr,exp,radix=10):
    output=len(arr)*[0]
    count=radix*[0]
    
    for i in arr:
        idx=(i//exp)%radix
        count[idx]+=1
        
    for i in range(1,radix):
        count[i]+=count[i-1]
        
    for i in arr[::-1]:
        idx=(i//exp)%radix
        output[count[idx]-1]=i
        count[idx]-=1
        
    for i in range(len(output)):
        arr[i]=output[i]

def radix_sort(arr):
    exp=1
    max_num=max(arr)
    while max_num//exp>0:
        counting_sort(arr,exp=exp)
        exp*=10

# Usage example
arr = [0,3,7,2,5,8,4,6,0,1]
radix_sort(arr)
print("Sorted array:", arr)




def counting_sort(arr, exp,radix=10):
    n = len(arr)
    output = [0] * n
    count = [0] * radix

    # Count the occurrences of each digit at the current place value
    for i in arr:
        idx=(i//exp)%radix
        count[idx]+=1


    # Calculate the cumulative count for each digit
    for i in range(1, radix):
        count[i] += count[i - 1]

    # Build the sorted output array
    for i in arr[::-1]:
        idx=(i//exp)%radix
        output[count[idx]-1]=i
        count[idx]-=1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)

    exp = 1
    while max_value // exp > 0:
        # Use counting sort on each digit's place value
        counting_sort(arr, exp)
        exp *= 10


radix_sort(arr)
print("Sorted array:", arr)
