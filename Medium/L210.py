class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res, vis, in_degree, q, adj = [], set(), [0] * numCourses, deque(), defaultdict(list)

        for p in prerequisites:
            in_degree[p[0]] += 1
            adj[p[1]].append(p[0])

        for i in range(numCourses):
            if not in_degree[i]:
                q.append(i)

        while q:
            size = len(q)
            for _ in range(size):
                n = q.popleft()
                if n in vis:
                    continue
                res.append(n)
                vis.add(n)

                for c in adj[n]:
                    in_degree[c] -= 1
                    if not in_degree[c]:
                        q.append(c)

        return res if numCourses == len(vis) else []
