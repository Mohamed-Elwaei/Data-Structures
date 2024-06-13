def select(A, p, r, i):
    while (r - p + 1) % 5 != 0:
        for j in range(p + 1, r + 1):
            if A[p] > A[j]:
                A[p], A[j] = A[j], A[p]
        
        if i == 1:
            return A[p]
        
        p += 1
        i -= 1
        
    g = (r - p + 1) // 5  # number of 5-element groups
    
    for j in range(p, p + g):
        sort_group(A, j, g)
    
    group_medians = [A[j + 2 * g] for j in range(p, p + g)]
    x = select(A, 0, g - 1, (g // 2) + 1)  # Median of the group medians
    
    q = partition_around(A, p, r, x)  # Partition around the pivot
    
    k = q - p + 1
    
    if i == k:
        return A[q]
    elif i < k:
        return select(A, p, q - 1, i)
    else:
        return select(A, q + 1, r, i - k)


def sort_group(A, j, g):
    group = [A[j + g * k] for k in range(5)]
    group.sort()
    for k in range(5):
        A[j + g * k] = group[k]


def partition_around(A, p, r, x):
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


# Usage example:
numbers = [3, 7, 1, 10, 5, 2, 9, 4, 6, 8]
result = select(numbers, 0, len(numbers) - 1, 4)
print("Result:", result)
