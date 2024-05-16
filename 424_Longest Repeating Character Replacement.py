input = "AABABBA"
k= 2
# ans = 4
def characterReplacement(s:str,k:int)-> int:
    # dictinary to store the count of character
    count = {}
    # store the answer
    result = 0
    # store the max frquency length
    maxf = 0
    # left point
    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        maxf = max(maxf,count[s[r]])
        # check current window size minus maxf greater than k means invalid windows
        if (r-l+1) - maxf > k:
            count[s[l]]-=1
            l+=1
        else:
            result = max(result,r-l+1) 
        print(l,r,result)       
    return result        
ans =  characterReplacement(input,k)
print(ans)
