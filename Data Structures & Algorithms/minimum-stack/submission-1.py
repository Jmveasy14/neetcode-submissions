from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()

        

    def push(self, val: int) -> None:
        if not self.stack:
            #if the stack is empty this value is the minimum
            self.stack.append((val,val))
        else:
            curr_min = self.stack[-1][1]
            self.stack.append((val,min(val,curr_min)))
        
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

        

    def getMin(self) -> int:
        return self.stack[-1][1]
