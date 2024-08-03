class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        MOD = 10**9 + 7

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = 0

            # Single digit
            if s[i] == '*':
                res += 9 * dfs(i + 1)
            else:
                res += dfs(i + 1)

            # Two digits
            if i + 1 < len(s):
                if s[i] == '*':
                    if s[i + 1] == '*':
                        res += 15 * dfs(i + 2)  # "**" can be 11-19 and 21-26 (9 + 6 = 15)
                    else:
                        if '0' <= s[i + 1] <= '6':
                            res += 2 * dfs(i + 2)  # "*0"-"*6" can be 10-16 or 20-26
                        else:
                            res += dfs(i + 2)  # "*7"-"*9" can only be 17-19
                elif s[i + 1] == '*':
                    if s[i] == '1':
                        res += 9 * dfs(i + 2)  # "1*" can be 11-19
                    elif s[i] == '2':
                        res += 6 * dfs(i + 2)  # "2*" can be 21-26
                else:
                    if int(s[i:i + 2]) <= 26:
                        res += dfs(i + 2)

            memo[i] = res % MOD
            return memo[i]

        return dfs(0)
        
