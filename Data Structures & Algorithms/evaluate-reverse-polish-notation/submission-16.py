class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        result = 0
        #we check for integers, if we have an integer we append the values to the stack
        for val in tokens:
            
            try:
                integer = int(val)
                stack.append(integer)
            except:
                right = stack.pop()
                left = stack.pop()
                if val == '+':
                    stack.append(left + right)
                elif val == '-':
                    stack.append(left - right)

                elif val == '*':
                    stack.append(left*right)

                elif val == '/':
                    try:
                        stack.append(int(left/right))
                    except:
                        stack.append(left)
        
        return stack[0]


                
                


        