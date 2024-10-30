class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph, q = defaultdict(list), deque([source])
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        vis = set()
        while q:
            node = q.popleft()
            if node == destination:
                return True
            if node in vis:
                continue
            vis.add(node)
            for nei in graph[node]:
                q.append(nei)

        return False