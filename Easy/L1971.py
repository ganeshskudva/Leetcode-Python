from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: Build the graph as an adjacency list
        # Using defaultdict to store each node's neighbors for an undirected graph.
        # Time Complexity: O(E), where E is the number of edges
        # Space Complexity: O(V + E), where V is the number of vertices and E is the number of edges
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        # Step 2: Initialize a queue for Breadth-First Search (BFS) starting from the source node
        # Initialize the queue with the source node
        # Time Complexity: O(1) for initialization
        # Space Complexity: O(V) for storing nodes in the queue at the maximum breadth
        q = deque([source])

        # Step 3: Initialize a set to track visited nodes
        # This helps to prevent reprocessing nodes and avoid infinite loops
        # Time Complexity: O(1) for set initialization
        # Space Complexity: O(V) for storing visited nodes
        vis = set()

        # Step 4: Perform BFS until the queue is empty
        # Time Complexity: O(V + E), as we explore each node and edge once
        while q:
            # Pop the leftmost (current) node from the queue
            node = q.popleft()

            # If we've reached the destination node, return True as a path exists
            if node == destination:
                return True

            # If the node has been visited, skip to the next iteration
            if node in vis:
                continue

            # Mark the current node as visited to avoid revisiting
            vis.add(node)

            # Add all unvisited neighbors to the queue
            # Time Complexity for each append: O(1), each neighbor is added to the queue once
            for nei in graph[node]:
                if nei not in vis:
                    q.append(nei)

        # If we exhaust the queue without finding the destination, return False
        # Time Complexity: O(1)
        return False

# Overall Complexity Summary:
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# This is because we explore each node and edge once in the breadth-first search.
# Space Complexity: O(V + E), for storing the adjacency list, visited set, and queue.


## DFS
from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: Build the graph as an adjacency list
        # Using defaultdict to store each node's neighbors for an undirected graph.
        # Time Complexity: O(E), where E is the number of edges
        # Space Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        # Step 2: Initialize a set to track visited nodes
        # Time Complexity: O(1) for set initialization
        # Space Complexity: O(V) for storing visited nodes
        vis = set()

        # Step 3: Define a recursive DFS helper function to check if a path exists
        # Time Complexity: O(V + E) in total as we potentially visit every node and edge once
        # Space Complexity: O(V) for the recursion call stack in the worst case
        def solve(node=source):
            # If the current node is the destination, we've found a path
            if node == destination:
                return True
            
            # If the node has been visited, return False to avoid re-processing
            if node in vis:
                return False

            # Mark the current node as visited
            vis.add(node)
            found = False  # Initialize a flag to track if a path is found
            
            # Recursively check all neighbors
            # For each neighbor, attempt to find a path to the destination
            # Time Complexity: O(1) per neighbor visit due to set operations
            for nei in graph[node]:
                found = found or solve(nei)  # Recursive DFS call
                if found:  # If path found, no need to check further neighbors
                    break

            return found

        # Step 4: Initiate DFS from the source node and return the result
        # The final result indicates if a valid path exists between source and destination
        return solve()

# Overall Complexity Summary:
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# This is because we explore each node and edge once in the depth-first search.
# Space Complexity: O(V + E), for storing the adjacency list, visited set, and recursion stack.
