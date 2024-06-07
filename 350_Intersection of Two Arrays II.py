from typing import List
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    app_dic = {}
    for n in nums1:
        if n in app_dic:
            app_dic[n]+=1
        else:
            app_dic[n] = app_dic.get(n,0) + 1  

    for n in nums2:
        if n in app_dic:
            if app_dic[n] > 0:
                ans.append(n) 
                app_dic[n]-=1
    return ans  

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))  



#     def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#         ans = []
#         app_dic = {}
#         for n in nums1:
#             if n in app_dic:
#                 app_dic[n]+=1
#             else:
#                 app_dic[n] = app_dic.get(n,0) + 1  

#         for n in nums2:
#             if n in app_dic:
#                 ans.append(n) 
#                 app_dic[n]-=1
#                 if app_dic[n] == 0:
#                     del app_dic[n]

#         return ans 