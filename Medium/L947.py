class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        vis, num_islands = set(), 0

        def solve(s):
            vis.add(tuple(s))
            for st in stones:
                if tuple(st) not in vis:
                    if st[0] == s[0] or st[1] == s[1]:
                        solve(st)
        
        for st in stones:
            if tuple(st) not in vis:
                solve(st)
                num_islands += 1
        
        return len(stones) - num_islands
