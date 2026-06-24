class Solution:
    def isValid(self, s: str) -> bool:

        closing = {']':'[',')':'(','}':'{'}

        stack = []

        for char in s:
            if char in closing:
                #if there is something in the stack and the last element compliments it we will pop it otherwise we append it
                if stack and stack[-1] == closing[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
        