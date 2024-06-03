# 方法1
# 這個方法會使用格外的memory 因為創建新變數
def isPalindrome(s: str) -> bool:
    # remove all not alnum string
    newStr = ""
    for c in s:
        if c.isalnum():
            # covert to lowercase
            newStr += c.lower()
    return newStr == newStr[::-1] 

s = "A man, a plan, a canal: Panama" 
ans = isPalindrome(s)
print(ans)

# 方法2
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l,r = 0, len(s)-1
#         while l<r:
#             while l<r and not self.alphaNum(s[l]):
#                 l+=1
#             while r>l and not self.alphaNum(s[r]):
#                 r-=1   
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     def alphaNum(self,c:str) -> bool:
#         if (ord("A")<= ord(c) <= ord("Z")) or (ord("a")<= ord(c) <= ord("z")) or (ord("0")<= ord(c) <= ord("9")):
#             return True
#         else:
#             return False
        
