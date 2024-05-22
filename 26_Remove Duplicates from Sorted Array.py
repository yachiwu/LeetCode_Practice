# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
from typing import List
def removeDuplicates( nums: List[int]) -> int:
    l = 1
    for r in range(1,len(nums)):
        # num is not duplicate
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l +=1
    return  l  
nums = [0,0,1,1,1,2,2,3,3,4]
ans = removeDuplicates(nums)
print(ans)