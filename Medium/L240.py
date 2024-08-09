class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def solve(arr, lo, hi):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] == target:
                    return True
                if target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return False

        found = False
        for m in matrix:
            if m[0] <= target <= m[-1]:
                found = solve(m, 0, len(m) - 1)
                if found:
                    return True

        return False
