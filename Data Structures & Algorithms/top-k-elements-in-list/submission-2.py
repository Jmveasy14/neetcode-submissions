class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(nums)+1)] 

        
        #if we see a number that isnt in count we add the value to the hashmap
        #and set it to 1, if we see it again we increase by +1
        #afterwards we return the value in count with the highest valuer
        for n in nums:
            
            count[n] = 1+count.get(n,0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

