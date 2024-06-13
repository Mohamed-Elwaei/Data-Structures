def merge_sort(arr):

    if len(arr)<=1:
        return arr
    
    mid=len(arr) // 2

    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right= merge_sort(right)

    return merge(left, right)

def merge(left, right):

    l=r=0

    merged=[]
    while l<len(left) and r<len(right):
        if left[l]< right[r]:
            merged.append(left[l])
            l+=1
        
        else:
            merged.append(right[r])
            r+=1
    
    while l<len(left):
        merged.append(left[l])
        l+=1
    
    while r<len(right):
        merged.append(right[r])
        r+=1
    return merged


my_list = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_list = merge_sort(my_list)
print(sorted_list)
