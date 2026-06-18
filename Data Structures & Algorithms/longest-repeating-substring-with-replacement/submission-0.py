class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_f = 0
        max_len = 0
        for right in range(len(s)):
            # 1. Add current char to map
            char = s[right]
            count[s[right]] = count.get(s[right],0) + 1
    # 2. Update max_len (max frequency of any single char in max_f)
            max_f = max(max_f,count[char])    
    # 3. WHILE the max_f is invalid (max_f_size - max_f > k):
            while (right - left +1 ) - max_f > k :
            #- Shrink the max_f by moving left forward
                count[s[left]] -=1
                left+=1
            # - Update the count map for the character being removed
            #    - left += 1
            max_len = max(max_len,right - left + 1)
    
    # 4. Now the max_f is guaranteed to be valid! 
    #    Update max_len = max(max_len, right - left + 1)

        return(max_len)
            

            
