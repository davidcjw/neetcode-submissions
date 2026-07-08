class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter -> defaultdict(int)]
        # {5: 10, 1000: 12, 234: 99}
        res = defaultdict(int)
        for i in nums:
            res[i] += 1

        # sort based on value
        res = sorted(res.items(), key=lambda item: item[1], reverse=True)
        print(res)
        new_res = []
        for x, y in res:
            new_res.append(x)

        print(new_res)

        return new_res[:k]