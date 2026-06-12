class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()

        for num in nums:
            if num not in dupe:
                dupe.add(num)
            else:
                return True

        return False
        