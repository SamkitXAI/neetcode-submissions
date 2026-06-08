class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) == 0:
            return True
        
        s_chars = {}
        t_chars = {}

        for i in range(len(s)) :
            if s[i] in s_chars:
                s_chars[s[i]] += 1
            else:
                s_chars[s[i]] = 0

            if t[i] in t_chars:
                t_chars[t[i]] += 1
            else:
                t_chars[t[i]] = 0
        
        if s_chars == t_chars:
            return True
        return False