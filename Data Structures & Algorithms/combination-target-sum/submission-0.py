class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, arr):
            # exit condition: if sum(arr) == target
            if sum(arr) == target:
                res.append(arr.copy())
                return
            elif i >= len(nums) or sum(arr) > target:
                return
            
            arr.append(nums[i])
            dfs(i, arr)
            arr.pop()
            dfs(i+1, arr)
            
        dfs(0, [])

        return res