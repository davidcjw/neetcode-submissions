class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force O(n^2)
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     res.append(product)
        # return res

        # using division operator
        zeroes = []
        total_product = 1
        for idx, num in enumerate(nums):
            if num == 0:
                zeroes.append(idx)
                continue
            total_product *= num
        
        if len(zeroes) >= 2:
            return [0] * len(nums)

        res = []
        if len(zeroes) == 1:
            for idx, num in enumerate(nums):
                if zeroes[0] == idx:
                    print(zeroes, total_product)
                    res.append(total_product)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(total_product // num)

        return res