class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        if len(s) == len(t) and sorted(s) == sorted(t):
            return True
        else:
            return False

        