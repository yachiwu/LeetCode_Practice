# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
# The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# abbaca
# 012345

# aaca
# 0123
def removeDuplicates(s: str) -> str:
    # i = 0
    # while i< len(s)-1:
    #     if s[i] == s[i+1]:
    #         s = s[:i]+ s[i+2:]
    #         i = max(i-1,0)
    #     else :
    #         i+=1
    # return s
    # time complexity : O(n^2)
    # space complexity : O(1)
    stack = []
    for cha in s:
        if stack and stack[-1] == cha:
            stack.pop()
        else:
            stack.append(cha)  
    return ''.join(stack)          
    # time complexity : O(n)
    # space complexity : O(n)
    

print(removeDuplicates("abbaca"))  # 输出: "ca"
print(removeDuplicates("azxxzy"))  # 输出: "ay"
