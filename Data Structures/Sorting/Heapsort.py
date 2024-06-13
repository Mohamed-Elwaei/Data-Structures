


def max_heapify(a,i):
    """Swap the node in question with the larger 
    of its two children and keep swapping
    until it reaches a position where it is either larger than its children or is a leaf node (childless).
    This procedure is called maxHeapify."""
    """max heapify assumes the children are maxheaps"""
    l=(i*2)+1
    r=(i*2)+2
    largest=i
    if r<len(a) and a[r]<a[i]:
        largest=r
    if l<len(a) and a[l]<a[largest]:
        largest=l
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        max_heapify(a,largest)
        
def build_max_heap(a):
    """
    1.Arbitrarily position the keys.
    2.For all the nodes starting from the lowest level to the top, run maxHeapify."""
    for i in range(len(a)//2,-1,-1):
        max_heapify(a,i)
        
def insert_max_heap(a,num):
    # worst case O(ceil(logn))
    # add as a leaf then compare with ancesstors
    """
    For insertion, we append a value to the end of the binary tree and then float it up, as long as necessary. This is exactly the same as increaseKey"""
    a.append(num)
    n = len(a) - 1
    parent = (n - 1) // 2

    while n > 0 and a[parent] < a[n]:
        a[parent], a[n] = a[n], a[parent]
        n = parent
        parent = (n - 1) // 2

        
def extraxt_max(a):
    """
    1.Swap the element at the extreme end of the heap with the root.
    2.Remove the value at the extreme end and return it as the maximum value.
    3.Sink in the root to the right place with maxHeapify."""
    a[0],a[-1]=a[-1],a[0]
    ret=a.pop()
    max_heapify(a,0)
    return ret

def heapsort(a):
    ret=[]
    while a:
        ret.append(extraxt_max(a))
    return ret


def draw_heap(heap):
    n = len(heap)
    max_level = (n // 2) - 1  # Last level with children

    for i in range(max_level + 1):
        level = " " * ((2 ** (max_level - i)) - 1)  # Initial spacing for each level
        spacing = " " * (2 ** (max_level - i))  # Spacing between nodes

        level_nodes = [str(heap[j]) if j < n else " " for j in range(2 ** i - 1, 2 ** (i + 1) - 1)]
        level_str = level + spacing.join(level_nodes)

        print(level_str)




import numpy.random
a=[10,9,8,7,6,5,4,3,2,1]

print(a)

build_max_heap(a)
draw_heap(a)
a=heapsort(a)

print(a)
