class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0
        
        for p,s in sorted(zip(position,speed), reverse = True):
            

            time = (target - p) / s
            
            stack.append(time)
            curr_time = stack[-1]

            if len(stack) >= 2 and curr_time <= stack[-2]:
                stack.pop()
            

        return len(stack)