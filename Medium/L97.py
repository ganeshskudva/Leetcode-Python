class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = defaultdict(bool)

        def solve(idx1=0, idx2=0, idx3=0):
            if idx3 == len(s1) + len(s2):
                return True
            key = (idx1, idx2)
            if key in dp:
                return dp[key]
            
            res = False
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                res = res or solve(idx1 + 1, idx2, idx3 + 1)
            if idx2 < len(s2) and s2[idx2] == s3[idx3]:
                res = res or solve(idx1, idx2 + 1, idx3 + 1)

            dp[key] = res
            return res

        return solve()
