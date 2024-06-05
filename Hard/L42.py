class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        def left_bound():
            ret = [0] * len(height)
            ret[0] = height[0]
            for i in range(1, len(height)):
                ret[i] = max(ret[i - 1], height[i])

            return ret

        def right_bound():
            ret = [0] * len(height)
            ret[-1] = height[-1]
            for i in range(len(height) - 2, -1, -1):
                ret[i] = max(ret[i + 1], height[i])

            return ret

        left, right, tot = left_bound(), right_bound(), 0
        for i in range(len(height)):
            tot += (min(left[i], right[i]) - height[i])

        return tot
        
