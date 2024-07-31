class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        def solve(left, right, mp=None):
            res = float('inf')
            if mp is None:
                mp = defaultdict(int)
            if (left, right) in mp:
                return mp[(left, right)]
            for i in range(len(cuts)):
                if cuts[i] <= left or cuts[i] >= right:
                    continue
                cost = right - left
                res = min(res, solve(left, cuts[i], mp) + cost + solve(cuts[i], right, mp))

            mp[(left, right)] = 0 if res == float('inf') else res
            return mp[(left, right)]

        return solve(0, n)
