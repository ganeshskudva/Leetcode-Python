class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mp = {}

        def solve(cur, amt):
            if cur == len(coins) or amt <= 0:
                return 1 if amt == 0 else 0

            key = (cur, amt)
            if key in mp:
                return mp[key]

            takeCoin, doNotTakeCoin = sys.maxsize, sys.maxsize
            if coins[cur] > amt:
                mp[key] = solve(cur + 1, amt)
            else:
                mp[key] = solve(cur, amt - coins[cur]) + solve(cur + 1, amt)

            return mp[key]

        return solve(0, amount)
