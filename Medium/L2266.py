class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 1000000007
        keys, dp = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4], defaultdict(int)

        def get_val(n):
            return ord(n) - ord('0')

        def solve(idx):
            if idx == len(pressedKeys):
                return 1
            if idx in dp:
                return dp[idx]

            cnt, num = 0, get_val(pressedKeys[idx])
            rep, i = keys[num], 0
            while i < rep and idx + i < len(pressedKeys) and pressedKeys[idx] == pressedKeys[idx + i]:
                cnt += solve(idx + 1 + i)
                cnt %= MOD
                i += 1

            dp[idx] = cnt
            return cnt

        return solve(0)
