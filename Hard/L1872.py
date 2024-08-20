class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        memo = {}

        # Compute prefix sums
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + stones[i - 1]

        def solve(prefix, index, alice_turn=True):
            if index == len(prefix) - 1:
                return prefix[index] if alice_turn else -prefix[index]
            if (index, alice_turn) in memo:
                return memo[(index, alice_turn)]

            if alice_turn:  # Alice's turn (maximize)
                ans1 = prefix[index] + solve(prefix, index + 1, not alice_turn)
                ans2 = solve(prefix, index + 1, alice_turn)
                memo[(index, alice_turn)] = max(ans1, ans2)
            else:  # Bob's turn (minimize)
                ans1 = -prefix[index] + solve(prefix, index + 1, not alice_turn)
                ans2 = solve(prefix, index + 1, alice_turn)
                memo[(index, alice_turn)] = min(ans1, ans2)

            return memo[(index, alice_turn)]

        return solve(prefix, 2)
