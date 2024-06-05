from typing import List
def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    # use the sliding window to find the min
    l , r = 0,k-1
    minValue =  float('inf')
    while r< len(nums):
        minValue = min(minValue,nums[r]-nums[l])
        l, r = l+1 , r+1
    return minValue 
nums = [9,4,1,7] 
k = 2
ans  = minimumDifference(nums,k)
print(ans)