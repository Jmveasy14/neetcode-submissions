class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')':'(', ']':'[', '}':'{'}
        stack = []
        #if we have an opening we add , if we find a  closing, we check if the corresponing opening is there and pop it

        for char in s:
            if stack and char in closing and closing[char] == stack[-1] :
                stack.pop()
            
            else:
                stack.append(char)
            
        return not stack
