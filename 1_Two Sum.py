class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i in range(len(nums)):
            result = target-nums[i]
            if result in num_dic:
                return [num_dic[result],i]
            else:
                num_dic[nums[i]] = i