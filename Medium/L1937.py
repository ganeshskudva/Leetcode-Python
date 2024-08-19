class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M = len(points)
        N = len(points[0])

        @cache
        def dp(r, c):
            if r == M - 1:
                return points[r][c]
            
            return points[r][c] + max(best_relative_right(r+1, c), best_relative_left(r+1, c))
        
        @cache
        def best_relative_left(r, c):
            """Returns the best value to the left side seen so far"""
            
            if c == 0:
                return dp(r, c)
            return max(dp(r, c), best_relative_left(r, c-1) - 1)
        
        @cache
        def best_relative_right(r, c):
            """Returns the best value to the right side seen so far"""

            if c == N-1:
                return dp(r, c)
            return max(dp(r, c), best_relative_right(r, c+1) - 1)
        
        return max(dp(0, c) for c in range(N))
