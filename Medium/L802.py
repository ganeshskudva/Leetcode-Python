from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # n: the number of nodes in the graph
        # mp: a reverse graph to track which nodes point to a given node
        # in_deg: array to store the in-degree (outgoing edges) of each node
        # Time Complexity: O(V + E), Space Complexity: O(V + E)
        n, mp, in_deg = len(graph), defaultdict(list), [0] * len(graph)
        
        # Step 1: Traverse the input graph to populate the reverse graph (mp) and calculate in-degrees (in_deg)
        # Time Complexity: O(V + E), where V is the number of nodes and E is the number of edges
        # Space Complexity: O(V + E) for storing the reverse graph and in-degree array
        for i, v in enumerate(graph):
            # in_deg[i] stores the number of outgoing edges from node i
            in_deg[i] = len(v)
            for e in v:
                # For each outgoing edge from i to e, reverse the direction and store it in mp
                mp[e].append(i)
        
        # Step 2: Initialize a queue with all terminal nodes (nodes with no outgoing edges, i.e., in_deg[i] == 0)
        # Time Complexity: O(V) to traverse all nodes once
        # Space Complexity: O(V) for the queue storing terminal nodes
        q = deque([i for i in range(n) if in_deg[i] == 0])
        
        # Step 3: Perform BFS to reduce in-degrees and identify safe nodes
        # Time Complexity: O(V + E), where each node and edge is processed exactly once
        # Space Complexity: O(V + E) to store the graph and the visited nodes in the queue
        while q:
            node = q.popleft()  # Get a node with 0 outgoing edges
            for nei in mp[node]:  # For each neighbor in the reverse graph
                in_deg[nei] -= 1  # Reduce the in-degree of its neighbors in the original graph
                if in_deg[nei] == 0:  # If a neighbor now has 0 outgoing edges, add it to the queue
                    q.append(nei)
        
        # Step 4: Return all nodes that have 0 outgoing edges after the processing (safe nodes)
        # Time Complexity: O(V) to check in_deg for all nodes
        # Space Complexity: O(V) to store the result list of safe nodes
        return [i for i in range(n) if not in_deg[i]]
