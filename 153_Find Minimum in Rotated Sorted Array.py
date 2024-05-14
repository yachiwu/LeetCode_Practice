# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
from typing import List
def findMid(nums:List[int])->int:
    l , r = 0, len(nums)-1
    result = nums[0] 
    while l<=r:
        m = (l+r)//2
        # search right
        if nums[m]>= nums[l]:
            result = min(result,nums[l])
            l  = m+1
        # search left
        else:
            result = min(result,nums[m])
            r = m-1
    return result

findMid([5,1,2,3,4])

