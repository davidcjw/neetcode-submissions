class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make use of complements
        seen = dict()
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], idx]
            seen[val] = idx
        return False