def binary_search(nums, target):
        n=len(nums)
        l,r=-1,n

        while r-l>1:
            mid = (l + r) // 2
            if nums[mid] == target:
                return target
            elif nums[mid] > target:
                r = mid
            else: 
                l=mid
        return l
        

# Example usage:
arr = nums = [1,3,5,6]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
