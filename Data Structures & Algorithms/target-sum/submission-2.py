class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        def dfs(i, running_sum):
            nonlocal count
            if i == len(nums)-1:
                if running_sum + nums[i] == target:
                    count += 1
                if running_sum - nums[i] == target:
                    count += 1
                return

            dfs(i+1, running_sum+nums[i])
            dfs(i+1, running_sum-nums[i])

        dfs(0, 0)

        return count
 