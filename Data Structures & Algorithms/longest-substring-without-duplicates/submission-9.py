class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1
        
        left = 0
        right = 1
        max_len = 0
        window = set()
        for right in range(len(s)):
            
            while s[right] in window:
                window.remove(s[left])
                left+=1
            
            window.add(s[right])

            max_len = max(max_len,len(window))
            
        return max_len
            

        