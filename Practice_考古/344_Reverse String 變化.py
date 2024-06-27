# input : test = [
#     "wx-yz",
#     "x-yz-mno-pqrs"
# ]
# Output: ["zy-xw","s-rq-pon-mzyx"]
# 字母順序反過來 符號不變
from  typing import List
def reverseString(s: str) -> str:
    l = 0
    r = len(s)-1
    string_list = list(s)
    while l<r:
        # 左右互換
        if string_list[l] != "-" and string_list[r] != "-":
            string_list[l], string_list[r] = string_list[r], string_list[l]
            l+=1
            r-=1
        # 單邊是"-" 跳過
        elif string_list[l] == "-":
            l+=1
        elif string_list[r] == "-":
            r-=1
    return ''.join(string_list)      
test = [
    "wx-yz",
    "x-yz-mno-pqrs"
 ]
for i in range(len(test)):
    ans = reverseString(test[i])
    print(ans)
        


