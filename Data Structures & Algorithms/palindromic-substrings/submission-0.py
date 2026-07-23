class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        #odd strings
        for i in range(len(s)):
            l,r = i,i

            while l >= 0 and r < len(s) and s[r] == s[l] :
                count+=1

                l-=1
                r+=1
        #even strings

            l,r = i,i+1
            while l >= 0 and r < len(s) and s[r] == s[l] :
                count+=1

                l-=1
                r+=1
        return count

        