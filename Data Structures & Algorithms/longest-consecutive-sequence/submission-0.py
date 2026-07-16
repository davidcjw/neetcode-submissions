class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of sequence has NO neighbours
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in nums:
                # start of sequence
                length = 1
                exit = False
                while not exit:
                    if num+1 not in nums:
                        exit = True
                        continue
                    length += 1
                    num += 1
                max_len = max(max_len, length)

        return max_len