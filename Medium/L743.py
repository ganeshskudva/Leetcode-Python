import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Create an adjacency list representation of the graph
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w  # u -> v with weight w

        # Priority queue (min-heap) where each element is (current distance, node)
        pq = [(0, K)]  # Start with the source node K and distance 0
        dist = {}  # Dictionary to track the shortest known distance to each node

        # Dijkstra's algorithm
        while pq:
            cur_dist, node = heapq.heappop(pq)  # Get the node with the smallest distance
            if node in dist:
                continue  # If we've already processed this node, skip it
            dist[node] = cur_dist  # Record the shortest distance to this node

            # Explore neighbors of the current node
            for neighbor, weight in graph[node].items():
                if neighbor not in dist:  # If we haven't visited this neighbor yet
                    new_dist = cur_dist + weight
                    heapq.heappush(pq, (new_dist, neighbor))  # Push the new distance and neighbor to the priority queue

        # If we reached all nodes, return the max distance; otherwise, return -1
        return max(dist.values()) if len(dist) == N else -1

# Time Complexity (TC): O(E * log(V)), where E is the number of edges and V is the number of vertices.
#   - Each node can be processed once, and for each node, we process all its edges. Each edge leads to a push or pop operation in the priority queue, which takes O(log V) time.
#   - The graph building process (adjacency list creation) takes O(E).

# Space Complexity (SC): O(V + E), where V is the number of vertices and E is the number of edges.
#   - We store the graph in an adjacency list (O(E)), the priority queue can grow up to size O(V), and we track the distances to each node in the dist dictionary (O(V)).
