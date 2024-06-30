# input  = ["aa","zaaz","zyaay"]
# ans = ["","","z"]
def removeDuplicates(s: str) -> str:
    stack = []
    for cha in s:
        if stack and stack[-1] == cha:
            stack.pop()
        else:
            stack.append(cha)  
    return ''.join(stack)          
    # time complexity : O(n)
    # space complexity : O(n)
input  = ["aa","zaaz","zyaay"]
ans = []
for word in input:
    ans.append(removeDuplicates(word))
print(ans)

