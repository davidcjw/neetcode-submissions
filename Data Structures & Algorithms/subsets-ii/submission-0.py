class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, subset):
            res.append(subset[:])
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                # prevent same number from being chosen twice
                if i > start and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
        
        dfs(0, [])
        return res