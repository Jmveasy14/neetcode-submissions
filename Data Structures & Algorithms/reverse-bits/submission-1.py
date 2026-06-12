class Solution:
    def reverseBits(self, n: int) -> int:

        n = bin(n)[2:]

        n = n[::-1]

        n = str(n)

        while len(n) <32:
            n+='0'

        n = int(n,2)

        return n
        