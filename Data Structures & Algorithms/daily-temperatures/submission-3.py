class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        # res = []
        # for i in range(len(temperatures)):
        #     curr = temperatures[i]
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > curr:
        #             res.append(j-i)
        #             break
        #     if len(res) != i+1:
        #         res.append(0)
        
        # return res

        # O(n)
        res = [0] * len(temperatures)
        stack = []
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            stack.append((temp, idx))

        return res
