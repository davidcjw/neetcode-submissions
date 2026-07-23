class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = 1e9
        for num in nums:
            minNum = min(minNum, num)
        return minNum