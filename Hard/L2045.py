class Solution:
    def bfs(self, adj, time, change, n):
        dist1 = [sys.maxsize] * (n + 1)
        dist2 = [sys.maxsize] * (n + 1)
        dist1[1] = 0  # We can set node 1, dist1[1] = 0; as it's the minimum we have initially.
        # dist2[1] = 0; # It will give the Wrong Answer, as we don't have a second minimum time, so initially, we can't allocate dist2[1] to 0.

        # (dist, node)
        q = deque([(0, 1)])

        while q and dist2[n] == sys.maxsize:
            currentDist, node = q.popleft()

            # Wait if light is red, if odd.
            # light : green in [0, c),  [2c, 3c), ... 
            # red  in [c, 2c), [3c, 4c), ...
            if (currentDist // change) % 2 == 1:
                currentDist += change - currentDist % change

            for neighbor in adj[node]:
                if dist1[neighbor] > currentDist + time:
                    dist1[neighbor] = currentDist + time
                    q.append((dist1[neighbor], neighbor))
                elif dist2[neighbor] > currentDist + time and currentDist + time != dist1[neighbor]:
                    dist2[neighbor] = currentDist + time
                    q.append((dist2[neighbor], neighbor))

        return dist2[n]

    def secondMinimum(self, n, edges, time, change):
        graph = defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return self.bfs(graph, time, change, n)
