import numpy as np
from random import randint

def Quicksort(a, p, r, Partition):
    if p >= r:
        return
    pivot = Partition(a, p, r)
    Quicksort(a, p, pivot - 1, Partition)
    Quicksort(a, pivot + 1, r, Partition)

def RandomizedPartition(a, p, q):
    pivoti = randint(p, q)
    pivot = a[pivoti]
    a[pivoti], a[q] = a[q], a[pivoti]
    i = p - 1
    for j in range(p, q):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[q] = a[q], a[i + 1]
    return i + 1


a = np.random.randint(1, 1112, 10)
Quicksort(a, 0, len(a) - 1, RandomizedPartition)
print(a)
