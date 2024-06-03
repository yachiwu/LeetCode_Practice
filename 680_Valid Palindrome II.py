# Input: s = "aaaz"
# Output: true
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s)-1
        while l<r:
            if s[l]!= s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l+=1
            r-=1
        return True   
    # def validPalindrome(self, s: str) -> bool:
    #     l , r = 0 , len(s)-1
    #     while l<r:
    #         if s[l]!= s[r]:
    #             skipL = s[l+1:r+1]
    #             skipR = s[l:r]
    #             return (self.isPalindrome(skipL) or self.isPalindrome(skipR))
    #         l+=1
    #         r-=1
    #     return True  
    # def isPalindrome(self, s: str) -> bool:
    #     l,r = 0, len(s)-1
    #     while l<r:
    #         while l<r and not s[l].isalnum():
    #             l+=1
    #         while r>l and not s[r].isalnum():
    #             r-=1   
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

sol = Solution()
result = sol.validPalindrome("aaaz")
print(result)
