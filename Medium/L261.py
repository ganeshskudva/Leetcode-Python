class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (n - 1) != len(edges):
            return False

        q, vis, adj = deque(), set(), defaultdict(list)
        parent = [-1] * n
        q.append(0)

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        while q:
            node = q.popleft()
            vis.add(node)
            for nei in adj[node]:
                if nei not in vis:
                    parent[nei] = node
                    q.append(nei)
                elif nei != parent[node]:
                    return False

        return len(vis) == n
