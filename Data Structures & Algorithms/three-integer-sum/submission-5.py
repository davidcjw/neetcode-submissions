class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # maintain two pointers l and r
        # and also maintain a seen set
        # [-4,-1,-1,0,1,2]
        nums.sort()
        res = []

        for i in range(len(nums)):
            # skip duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[l],nums[r],nums[i]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
        
        return res
