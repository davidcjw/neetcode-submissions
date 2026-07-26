class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j, subset)

        
        dfs(0, [])
        return res