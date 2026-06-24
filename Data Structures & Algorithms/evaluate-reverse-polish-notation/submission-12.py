class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        
        

        stack = []
        total = 0
        for s in tokens:
            #if we find a number we add it to the stack
            try: 
                integer = int(s)
                stack.append(integer)
            except:
                right = stack.pop()
                left = stack.pop()
                
            #if we find an operator, we need to apply it to whats in the stack
                if s == '+':
                    stack.append(left+right)

                elif s == '-':
                    stack.append(left-right)

                elif s == '*':
                    stack.append(left*right)
            
                elif s == '/':
                    stack.append(int(left/right))
                    

        return stack[0]