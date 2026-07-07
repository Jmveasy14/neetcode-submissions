class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)
        for current_i,current_t in enumerate(temperatures):
            while stack and current_t > temperatures[stack[-1]]:
                popped_i = stack.pop()
                result[popped_i] = current_i - popped_i
            
            stack.append(current_i)
        
        return result