class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) - maintain left and right pointers
        l, r = 0, len(numbers)-1
        while numbers[l] + numbers[r] != target:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            else:
                l += 1
            
        return [l+1, r+1]