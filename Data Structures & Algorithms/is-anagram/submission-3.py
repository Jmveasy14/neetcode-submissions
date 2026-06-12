class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False

        for char in range(len(s)):
            if s[char] == t[char]:
                continue
            else:
                return False
        
        return True