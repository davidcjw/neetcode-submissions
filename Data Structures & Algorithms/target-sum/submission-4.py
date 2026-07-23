class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, running_sum):
            if i == len(nums):
                return 1 if running_sum == target else 0

            if (i, running_sum) in memo:
                return memo[(i, running_sum)]
            
            result = dfs(i+1, running_sum+nums[i]) + dfs(i+1, running_sum-nums[i])
            return result

        return dfs(0, 0)
 