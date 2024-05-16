# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2  = 82
# 8^2  + 2^2  = 68
# 6^2 + 8^2  = 100
# 1^2  + 0^2  + 0^2  = 1


# Input: n = 2
# Output: false
# Explanation:
# 2^2 = 4
# 4^2 = 16
# 1^2 + 6^2 = 37
# 3^2 + 7^2 = 58
# 5^2 + 8^2 = 89
# 8^2 + 9^2 = 145
# 1^2 + 4^2 + 5^2 = 42
# 4^2 + 2^2 = 20
# 2^2 + 0^2 = 4 開始重複

def sumOfSquares(n):
    output = 0
    while n:
        digit = n % 10
        digit = digit**2
        output += digit
        n = n // 10
    return output

def isHappy(n: int) -> bool:
    visit = set()
    while n not in visit:
        visit.add(n)
        n = sumOfSquares(n)
        if n == 1:
            return True
    return False

ans = isHappy(19)
print(ans)

ans = isHappy(2)
print(ans)