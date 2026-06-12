class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(map(str,digits))

        num = int(num)

        num+=1

        num = str(num)

        num = list(num)

        return num
        