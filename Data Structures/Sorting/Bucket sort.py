import numpy as np

def bucket_sort(A):
    # Initialize a list of empty buckets
    buckets = [[] for _ in A]
    
    # Find the maximum and minimum values in the input list
    Max, Min = max(A), min(A)
    
    # Initialize an empty list to store the sorted result
    ans = []
    
    # Calculate the range of values in the input list
    Range = Max - Min
    
    # Distribute elements into buckets based on their values
    for i in A:
        # Calculate the index of the bucket for the current element
        idx = int(((i - Min) * (len(buckets) )) / (Range+1))
        
        # Add the element to the corresponding bucket
        buckets[idx].append(i)
    
    # Sort each bucket individually (you can use a more efficient sorting algorithm)
    for b in buckets:
        ans.extend(sorted(b))
    
    # Return the final sorted result
    return ans

import numpy as np

# Generate an array of 10 random floating-point numbers between 0 and 1
random_floats = np.random.rand(5)

# Generate an array of 10 random integers between 1 and 100
random_integers = np.random.randint(-10, 10, 5)

# Concatenate (mix) the two arrays together
mixed_array = np.concatenate((random_floats, random_integers))

mixed_array=bucket_sort(mixed_array)
print(mixed_array)