from typing import List
from collections import Counter
def uniqueOccurrences(arr: List[int]) -> bool:
    occurrence = Counter(arr)
    count_values = list(occurrence.values())
    unique_counts = set(count_values)
    
    return len(count_values) == len(unique_counts)
       
arr = [1,2,2,1,1,3,3]
ans = uniqueOccurrences(arr)
print(ans)




# 不使用Counter and set
# from typing import List

# def uniqueOccurrences(arr: List[int]) -> bool:
#     occurrence = {}
    
#     # 遍歷列表，計算每個元素的出現次數
#     for num in arr:
#         occurrence[num] = occurrence.get(num, 0) + 1
    
#     # 檢查出現次數是否唯一
#     count_values = list(occurrence.values())
#     seen_counts = []
    
#     for count in count_values:
#         if count in seen_counts:
#             return False
#         seen_counts.append(count)
    
#     return True
