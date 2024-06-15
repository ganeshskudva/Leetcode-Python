class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res, max_right = [0] * len(arr), 0
        res[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            max_right = max(max_right, max(arr[i+ 1], res[i + 1]))
            res[i] = max_right

        return res
