class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(startIdx, nums, remaining):
            if remaining == 0:
                res.append(nums[:])
                return
            
            for i in range(startIdx, len(candidates)):
                if i > startIdx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remaining:
                    break
                nums.append(candidates[i])
                dfs(i+1, nums, remaining-candidates[i])
                nums.pop()
        
        dfs(0, [], target)
        return res