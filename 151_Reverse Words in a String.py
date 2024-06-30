# Input: s = "the sky is blue"
# Output: "blue is sky the"

def reverseWords(s: str) -> str:
    # remove leading spaces  or use s.strip()
    while s and s[0] == " ":
        s[1:]
    while s and s[-1] == " ":
        s = s[:-1]        

    # split by space
    words = s.split()
    # reverse the word
    words = words [::-1]
    return ' '.join(words)

s = "the sky is blue"
ans = reverseWords(s)
print(ans)


