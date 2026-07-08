class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return as soon as we find a duplicate
        # time - O(n)
        # space - O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
