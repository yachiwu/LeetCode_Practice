class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted_word = "".join(sorted(s))
            result[sorted_word].append(s)   
        return result.values()