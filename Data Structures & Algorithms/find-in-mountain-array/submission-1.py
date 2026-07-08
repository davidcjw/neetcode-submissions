class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # Step 1: Find peak index
        lo, hi = 1, n - 2
        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1  # still ascending, peak is to the right
            else:
                hi = mid      # descending or at peak, peak is here or left
        peak = lo
        
        # Step 2: Binary search ascending left side [0, peak]
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        # Step 3: Binary search descending right side [peak+1, n-1]
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:  # descending order, so go right for smaller
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1