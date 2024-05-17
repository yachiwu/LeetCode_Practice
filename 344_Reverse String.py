# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

from  typing import List
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l , r = 0 ,len(s)-1
    while l<r:
        s[l],s[r] = s[r],s[l]
        l+=1
        r-=1
    return s  

s = ["h","e","l","l","o"]
ans = reverseString(s) 
print(ans)
        