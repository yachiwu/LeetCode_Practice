class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            s_dic[s[i]] = s_dic.get(s[i], 0) + 1
            t_dic[t[i]] = t_dic.get(t[i], 0) + 1
        for cha in s_dic:
            if s_dic[cha] != t_dic.get(cha,0):
                return False

        return True