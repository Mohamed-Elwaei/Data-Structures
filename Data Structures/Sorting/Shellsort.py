import random
import math
import time

def shellsort(arr, sequence_generator):
    gaps = []
    n = len(arr)
    sequence_generator(n, gaps)

    for gap in gaps:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = key

def shell_sequence(n, gaps):
    while n > 0:
        n >>= 1
        gaps.append(n)

def hibbard_sequence(n, gaps):
    k = 1
    gap = 0
    while gap < n:
        gap = (1 << k) - 1
        gaps.append(gap)
        k += 1

def knuth_sequence(n, gaps):
    gap = 1
    while gap < n:
        gaps.append(gap)
        gap = math.floor((gap ** 3 + 1) / 2)

def gonnet_sequence(n, gaps):
    gap = n
    while gap > 0:
        gaps.append(gap)
        gap //= 2

def sedgewick_sequence(n, gaps):
    gaps.append(1)
    k = 1
    gap = 0
    while gap < n:
        gap = (1 << k) + 3 * (1 << (k - 1)) + 1
        gaps.append(gap)
        k += 1

if __name__ == "__main__":
    SIZE = 10000  # Size of the array

    # Generate a shuffled list of integers from 1 to SIZE
    arr = list(range(1, SIZE + 1))
    random.shuffle(arr)

    # Perform shellsort with different increment sequences and measure the time
    copy_arr = []

    # Shell's original sequence
    copy_arr = arr[:]  # Make a copy of the original array
    start_time = time.time()
    shellsort(copy_arr, shell_sequence)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken by Shell's original sequence:", elapsed_time, "seconds")

    # Hibbard's increments
    copy_arr = arr[:]  # Reset the array
    start_time = time.time()
    shellsort(copy_arr, hibbard_sequence)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken by Hibbard's increments:", elapsed_time, "seconds")

    # Knuth's increments
    copy_arr = arr[:]  # Reset the array
    start_time = time.time()
    shellsort(copy_arr, knuth_sequence)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken by Knuth's increments:", elapsed_time, "seconds")

    # Gonnet's increments
    copy_arr = arr[:]  # Reset the array
    start_time = time.time()
    shellsort(copy_arr, gonnet_sequence)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken by Gonnet's increments:", elapsed_time, "seconds")

    # Sedgewick's increments
    copy_arr = arr[:]  # Reset the array
    start_time = time.time()
    shellsort(copy_arr, sedgewick_sequence)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time taken by Sedgewick's increments:", elapsed_time, "seconds")

