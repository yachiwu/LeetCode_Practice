# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
from typing import List
def  getConcatenation(nums: List[int] ) -> List[int]:
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans  
 
nums = [1,2,1]
ans = getConcatenation(nums)    
print(ans) 

