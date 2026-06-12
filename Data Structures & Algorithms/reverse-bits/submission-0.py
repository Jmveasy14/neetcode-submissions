class Solution:
    def reverseBits(self, n: int) -> int:
        #we convert n into a binary integer and then skip the first 2 characters
        n = bin(n)[2:]

        #then we reverse it
        n = n[::-1]

        #after we add as many 0s need up to 32
        n = str(n)
        while len(n) < 32:
            n += '0'

        n = int(n,2)

        return n
        