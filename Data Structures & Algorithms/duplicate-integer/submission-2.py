class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_found = set()
        
    #we make a list to keep track of the numbers

    #If the number is not in the dictionary, we add it, then continue
    #If the number is in the dictionary, we found a duplicate and return true
        for num in nums:
            if num in nums_found:
                return True
            else:
                nums_found.add(num)
    
        return False
     