class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for char in s:
            if char in lookup:
                stack.append(char)
            elif len(stack)==0 or lookup[stack.pop()] != char:
                return False  
        
        return True if not stack else False