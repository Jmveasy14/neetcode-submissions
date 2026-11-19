class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        seen = {}

        for s in range(len(strs)):
            sorted_s = "".join(sorted(strs[s]))
            if sorted_s in seen:
                seen[sorted_s].append(strs[s])
            else:
                seen[sorted_s] = [strs[s]]

        return list(seen.values())
        
