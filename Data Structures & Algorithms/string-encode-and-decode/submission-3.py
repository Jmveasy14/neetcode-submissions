class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        #iterate through encoded list and if the char is '#', we separate the characters between that and the next
        res = []
        i = 0
        # '4#neet'
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])

            res.append(s[j+1:j+1 + length])
            #moves to the next word
            i = j +1 + length
        return res

