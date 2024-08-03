class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        res, mp = [], defaultdict(set)
        for r in regions:
            for i in range(1, len(r)):
                mp[r[0]].add(r[i])

        def solve(node):
            curr = (0, 0)
            if node == region1:
                curr = (1, 0)
            elif node == region2:
                curr = (0, 1)

            for nei in mp[node]:
                ret = solve(nei)
                curr = (curr[0] or ret[0], curr[1] or ret[1])
                if all(curr):
                    res.append(node)
                    return 0, 0

            return curr
        solve(regions[0][0])
        return res[0]
