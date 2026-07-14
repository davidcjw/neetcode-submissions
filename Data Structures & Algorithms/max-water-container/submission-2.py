class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # greedy
        l, r = 0, len(heights)-1
        max_area = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, curr_area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            print(max_area)
        return max_area
