class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # division way
        # 1 zero, only that 0 will be non-zero in the output array
        # if 2 zeroes, then all will be zero, return
        # otherwise no zeroes, we can take output[i] == total_product / nums[i]
        zeroes = []
        total_product = 1
        for idx, num in enumerate(nums):
            if num == 0:
                zeroes.append(idx)
                continue

            total_product *= num
        
        output = [0] * len(nums)

        if len(zeroes) >= 2:
            return output

        if len(zeroes) == 1:
            non_zero_idx = zeroes.pop()
            output[non_zero_idx] = total_product
            return output
        
        for idx, num in enumerate(nums):
            output[idx] = total_product // nums[idx]

        return output