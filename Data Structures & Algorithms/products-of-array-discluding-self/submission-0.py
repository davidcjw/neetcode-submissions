class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive way
        output = [0] * len(nums)
        for i, num in enumerate(nums):
            product = None
            for j, num in enumerate(nums):
                if i == j:
                    continue
                
                if product == None:
                    product = num
                    continue

                product *= num
            
            output[i] = product

        return output
