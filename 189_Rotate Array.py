# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

from  typing import List
def rotate(nums: List[int], k: int) -> List[int]:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    l ,r = 0 , len(nums)-1
    # reverse the entire array
    while l<r:
        nums[l], nums[r] = nums[r],nums[l]
        l +=1
        r -=1
    # reverse the top k 
    l ,r = 0, k-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l +=1 
        r-=1
    # reverse the remaining array
    l ,r = k, len(nums)-1
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l +=1 
        r -=1   
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
ans = rotate(nums,k)
print(ans)

# another solution
# def rotate(self, nums: List[int], k: int) -> None:
#     k = k % len(nums)
#     # Reverse the entire array
#     nums[:] = nums[::-1]
#     # Reverse the first k elements
#     nums[:k] = nums[:k][::-1]
#     # Reverse the remaining elements
#     nums[k:] = nums[k:][::-1]