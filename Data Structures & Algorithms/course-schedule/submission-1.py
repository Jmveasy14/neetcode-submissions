class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        visited = set()

        for crs,pre in prerequisites:
            adj[crs].append(pre)
        
        state = [0] * numCourses

        def dfs(crs):
            #If the starting one is the course before the prereq, its impossible
            if state[crs] == 1: 
                return False
            if state[crs] == 2:
                return True
            
            if state[crs] == 0:
                state[crs] = 1
                for pre in adj[crs]:
                    if not dfs(pre):
                        return False
            
            state[crs] = 2
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        