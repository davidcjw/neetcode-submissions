class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [1,5,2,10]
        minVal = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > minVal:
                maxProfit = max(maxProfit, prices[i] - minVal)
            else:
                minVal = prices[i]
        
        return maxProfit