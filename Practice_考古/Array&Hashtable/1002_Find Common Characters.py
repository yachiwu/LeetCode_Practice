from typing import List
from collections import Counter
def commonChars(words: List[str]) -> List[str]:
    # initilize the first word dictionry
    cnt = Counter(words[0])
    # Iterate over the rest of the word, find the same charactor in both of them
    for i in range(1,len(words)):
        current_cnt = Counter(words[i])
        for c in cnt:
            cnt[c] = min(cnt[c],current_cnt[c])        
    res = []
    for c in cnt:
        for i in range(cnt[c]):
            res.append(c)
    return res        

    

words = ["bella","label","roller"]
ans = commonChars(words)
print(ans)


# def count_chars(word):
#     char_count = {}
#     for char in word:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#     return char_count

# def commonChars(words: List[str]) -> List[str]:
#     # initilize the first word dictionry
#     common_count = count_chars(words[0])
#     # Iterate over the rest of the word, find the same charactor in both of them
#     for word in words[1:]:
#         current_word_count = count_chars(word)
#         for char in common_count:
#             if char in current_word_count:
#                 common_count[char] = min(common_count[char],current_word_count[char])
#             else:
#                 common_count[char] = 0 
#     result = []
#     for key, value in common_count.items():
#         result.extend([key] * value)    
#     return result      


# words = ["bella","label","roller"]
# ans = commonChars(words)
# print(ans)



