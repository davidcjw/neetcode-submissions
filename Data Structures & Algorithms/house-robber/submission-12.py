class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]
        # dp = [2,9,0,0,0]
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            dp[i] = dp[i-1] if dp[i-1] >= nums[i] + dp[i-2] else nums[i] + dp[i-2]
        return max(dp[len(nums)-1], dp[len(nums)-2])
