class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n^2)
        for idx_x, x in enumerate(numbers):
            for idx_y, y in enumerate(numbers):
                if x + y == target:
                    return [idx_x+1, idx_y+1]
