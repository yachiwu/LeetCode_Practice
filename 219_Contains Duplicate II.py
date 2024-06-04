# Input: nums = [1,2,3,1], k = 3
# Output: true
from typing import List
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    # index_dic = {}
    # for index, num in enumerate(nums):
    #     # encouter duplicate, calculate current index and last index of the num
    #     if num in index_dic and index-index_dic[num] <=k:
    #         return True
    #     # first time , num not in the dic condition
    #     index_dic[num] = index
    # return False

    window = set()
    L = 0
    for R in range(len(nums)):
        if R-L > k:
            window.remove(nums[L])
            L+=1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False    
nums = [1,2,3,3]
k=2
print(containsNearbyDuplicate(nums,k))
