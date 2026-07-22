class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [4,5,3,3,2,1,1]
        # [1,2,3]
        # [-1,2,3]
        dp = [-1] * len(cost)
        dp[-1], dp[-2] = cost[-1], cost[-2]
        for i in range(len(cost)-3,-1,-1):
            dp[i] = min(dp[i+1]+cost[i], dp[i+2]+cost[i])
        return min(dp[0], dp[1])