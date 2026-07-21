class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # c = Counter(nums)
        # for k, v in c.items():
        #     if v > 1:
        #         return k
        
        # Optimal using O(n) time and O(1) space
        # Floyd's algorithm for cycle detection
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        
        return slow