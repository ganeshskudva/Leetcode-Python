class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp, mp = defaultdict(int), collections.Counter(dictionary)

        def solve(idx):
            if idx >= len(s):
                return 0
            if idx in dp:
                return dp[idx]

            min_extra, curr_extra = len(s), 0
            for cut_idx in range(idx, len(s)):
                curr = s[idx:cut_idx + 1]

                curr_extra = 0 if curr in mp else len(curr)
                min_extra = min(min_extra, curr_extra + solve(cut_idx + 1))

            dp[idx] = min_extra
            return min_extra

        return solve(0)
