class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)
        LIS = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):  # look behind i
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        
        return max(LIS)
