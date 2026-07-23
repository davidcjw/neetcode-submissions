class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            arr.extend(row)

        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                l = mid + 1
            if arr[mid] > target:
                r = mid - 1
        
        return False

