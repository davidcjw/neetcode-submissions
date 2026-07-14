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
        # zeroes = []
        # total_product = 1
        # for idx, num in enumerate(nums):
        #     if num == 0:
        #         zeroes.append(idx)
        #         continue
        #     total_product *= num
        
        # if len(zeroes) >= 2:
        #     return [0] * len(nums)

        # res = []
        # if len(zeroes) == 1:
        #     for idx, num in enumerate(nums):
        #         if zeroes[0] == idx:
        #             print(zeroes, total_product)
        #             res.append(total_product)
        #         else:
        #             res.append(0)
        # else:
        #     for num in nums:
        #         res.append(total_product // num)

        # return res

        # prefix and postfix method
        prefix = [nums[0]]
        postfix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i-1])
        
        j = 0
        for i in range(len(nums)-2, -1, -1):
            print(i)
            postfix.append(nums[i] * postfix[j])
            j += 1

        postfix = postfix[::-1]

        res = []
        for i in range(len(nums)):
            if i > 0 and i < len(nums)-1:
                res.append(prefix[i-1] * postfix[i+1])
            elif i == 0:
                res.append(postfix[i+1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
        print(res)
        
        return res