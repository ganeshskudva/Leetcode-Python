class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res, mp = [[] for _ in range(n)], defaultdict(list)

        for start, dest in edges:
            mp[dest].append(start)

        def solve(node, st):
            if node in st:
                return
            st.add(node)

            for nei in mp[node]:
                solve(nei, st)

        for k in list(mp.keys()):
            children = set()
            solve(k, children)
            for c in sorted(children):
                if c == k:
                    continue
                res[k].append(c)

        return res
        
        
