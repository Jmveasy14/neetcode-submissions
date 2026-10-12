class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        longest = 0
        visited = set()
        visited.add(s[l])
        #sliding window
        while r < len(s):
            #add characters to a set to keep track of unique values
            if s[r] not in visited:
                visited.add(s[r])
                
            elif s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l+=1
                visited.add(s[r])
            longest = max(longest, r - l+ 1)
            #when we find something thats already in there, we calculate the length of the window
                
            r+=1
        return longest
            


        
    
        
        #move left to right
