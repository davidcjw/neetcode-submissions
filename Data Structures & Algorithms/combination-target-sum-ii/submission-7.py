class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, nums, remaining):
            if remaining == 0:
                res.append(nums[:])
                return
            if i == len(candidates) or candidates[i] > remaining:
                return
            
            nums.append(candidates[i])
            dfs(i+1, nums, remaining-candidates[i])
            nums.pop()

            # find next num that is not the same as i
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, nums, remaining)
        
        dfs(0, [], target)
        return res