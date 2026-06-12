class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ''
        for char in range(len(s)-1,-1,-1):
            if not s[char].isalnum():
                continue
            new_s+=s[char]
        new_s = new_s.lower()
        print(new_s)
        print(new_s[::-1])
        if new_s == new_s[::-1]:
            return True

        return False
            

            
        