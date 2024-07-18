class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n, to_routes = len(routes), defaultdict(set)
        for i in range(n):
            for r in routes[i]:
                to_routes[r].add(i)

        q, seen, seen_routes = deque(), set(), [False] * n
        q.append((source, 0))
        seen.add(source)

        while q:
            stop, bus = q.popleft()
            if stop == target:
                return bus
            for i in to_routes[stop]:
                if seen_routes[i]:
                    continue
                for j in routes[i]:
                    if j not in seen:
                        seen.add(j)
                        q.append((j, bus + 1))
                seen_routes[i] = True
        
        return -1
