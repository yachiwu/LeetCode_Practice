# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


from  typing import List
def searchInsert(nums: List[int], target: int) -> int:
    l = 0 
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]> target:
            r = mid-1
        elif nums[mid] < target:
            l = mid+1
        else:
            return mid
    return l        
nums = [1,3,5,6]
target = 2
ans = searchInsert(nums,target)
print(ans)