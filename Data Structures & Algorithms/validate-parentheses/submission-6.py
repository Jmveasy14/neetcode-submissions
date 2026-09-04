class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {')' : '(' , ']': '[', '}': '{'}
        stack = []
        
        
        for char in s:
            if char in parentheses:
                if stack and parentheses[char] == stack[-1]:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack


                    
        