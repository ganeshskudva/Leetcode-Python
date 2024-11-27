class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Create a mapping of edges using adjacency list
        mp = defaultdict(list)
        for i in range(n - 1):  # Initialize edges for a straight path
            mp[i].append(i + 1)

        def solve():
            # BFS to find the shortest path
            cnt, q, vis = 0, deque([0]), set()  # Initialize BFS variables
            while q:
                sz = len(q)  # Number of nodes to process at the current level
                for _ in range(sz):
                    node = q.popleft()
                    if node in vis:  # Skip visited nodes
                        continue
                    if node == n - 1:  # Found the target node
                        return cnt
                    vis.add(node)  # Mark the node as visited
                    for nei in mp[node]:  # Add neighbors to the queue
                        q.append(nei)
                cnt += 1  # Increment the distance counter

            return -1  # If no path exists, return -1

        res = []
        for src, dest in queries:
            # Add the query edge to the adjacency list
            mp[src].append(dest)
            res.append(solve())  # Solve the BFS for the updated graph

        return res

# Time Complexity (TC):
# Outer loop over queries is O(Q), where Q is the number of queries.
# Inside each query, a BFS traversal is performed:
# BFS complexity is O(V + E), where V = n (nodes) and E = edges in the graph.
# Total TC = O(Q * (V + E)) = O(Q * (n + E)).

# Space Complexity (SC):
# Space for the adjacency list `mp` is O(E).
# Space for the BFS queue `q` and visited set `vis` is O(V) = O(n).
# Total SC = O(E + n).
