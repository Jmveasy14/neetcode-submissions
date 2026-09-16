class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')':'(' , ']':'[', '}': '{'}
        stack = []
        for char in s:
            if stack and char in closing:
                if stack[-1] == closing[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
        
        return not stack