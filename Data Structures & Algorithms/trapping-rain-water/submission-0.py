class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Water can be trapped between two bars if:
        - the space between the two bars is strictly smaller than the
          smaller of the two bars e.g. 5, 2, 3; 2 < min(5,3) so
          the area is min(5,3)-2=1
        - there is a bar-dip-bar pattern i.e. consecutive increasing bars
          can't trap water. there has to be at least 1 space that dips
        
        While looking for the second bar to trap water, we continue
        finding a suitable bar as long as the subsequent bars are less
        than or equal to the current (first) bar

        Edge cases:
        - Only one bar, no water is trapped. (not really an edge case)
        - Decreasing only bars - no water should be trapped
        - Increasing only bars - no water should be trapped
        - Both sides have extremely high bars e.g. [10,0,1,0,2,0,3,0,4,0,10]
          1         1
          1         1
          1         1
          1         1
          1         1
          1         1
          1       1 1
          1     1 1 1
          1   1 1 1 1
          1_1_1_1_1_1
        """
        l, r = 0, len(height)-1
        area = 0
        leftMax, rightMax = height[l], height[r]
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
        
        return area
