# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# 寫法一
# from typing import List
# from collections import defaultdict 

def topKFrequent(nums: List[int], k: int) -> List[int]:
    frec_dic = defaultdict(int)
    for num in nums:
        frec_dic[num]+=1
       
    sorted_frec_dic= sorted(frec_dic.items(), key=lambda x: x[1],reverse=True)

    topKList = []
    for i in range(k):
        topKList.append(sorted_frec_dic[i][0])
    return topKList
# nums = [1,1,1,2,2,3]
# k = 2
# ans = topKFrequent(nums,k)     
# print(ans)



# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     count = {}
#     freq = [[]for i in range(len(nums)+1)]
#     for n in nums:
#         count[n] = 1+ count.get(n,0)
#     for n,c in count.items():
#         freq[c].append(n)
#     res = []
#     for i in range(len(freq)-1,0,-1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res) == k:
#                 return res

