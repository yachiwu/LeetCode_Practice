s = "MCMXCIV"
def romanToInt(s: str) -> int:
    roman = { "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    ans = 0
    for i in range(len(s)):
        # if the next cha value is greater then the current cha, it means the current is negtive
        # for example IX  = -1 + 5 becasue X is greater then I
        if i+1< len(s) and roman[s[i+1]]>roman[s[i]]:
            ans-= roman[s[i]]
        else:
            ans+= roman[s[i]]
    return ans   
print(romanToInt(s))