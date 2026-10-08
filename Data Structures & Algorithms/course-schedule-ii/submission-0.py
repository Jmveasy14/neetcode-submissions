class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        visited = set()
        res = []
        for course,prereq in prerequisites:
            adj[course].append(prereq)
        
        state = [0] * numCourses
        
        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True

            state[crs] = 1
            for val in adj[crs]:
                if not dfs(val):
                    return False
            state[crs] = 2
            res.append(crs)
            return True
                
                    

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res