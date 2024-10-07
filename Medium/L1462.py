from collections import defaultdict, deque
from typing import List, Set

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # in_deg: List to store the in-degree (number of prerequisites) for each course
        # adj: Adjacency list representing the graph where each course points to its dependent courses
        # prerequisites_map: A map to track all prerequisite courses for each course
        
        in_deg = [0] * n  # Tracks the in-degree (number of prerequisites) of each course
        adj = defaultdict(set)  # Adjacency list representing the graph
        prerequisites_map = defaultdict(set)  # Tracks all prerequisites for each course

        # Step 1: Build the graph and initialize the in-degree array
        # Time Complexity: O(E), where E is the number of edges (prerequisites)
        # Space Complexity: O(V + E), where V is the number of courses (nodes) and E is the number of edges (prerequisites)
        for pre in prerequisites:
            u, v = pre
            in_deg[v] += 1  # v depends on u, so increment v's in-degree
            adj[u].add(v)  # u -> v (u is a prerequisite for v)

        # Step 2: Initialize a queue with courses that have 0 in-degree (no prerequisites)
        # These courses can be taken immediately
        # Time Complexity: O(V), where V is the number of courses (nodes)
        # Space Complexity: O(V)
        queue = deque([i for i in range(n) if in_deg[i] == 0])

        # Step 3: Process each course using topological sorting (BFS)
        # Time Complexity: O(V + E), where V is the number of courses and E is the number of edges (prerequisites)
        # Space Complexity: O(V + E) for maintaining the adjacency list and prerequisites map
        while queue:
            course = queue.popleft()  # Process a course with 0 in-degree
            for next_course in adj[course]:  # For each course dependent on the current course
                # Update the prerequisites of next_course by adding all prerequisites of the current course
                prerequisites_map[next_course].add(course)
                prerequisites_map[next_course].update(prerequisites_map[course])

                # Reduce the in-degree of the next course
                in_deg[next_course] -= 1
                # If the in-degree becomes 0, add the next course to the queue
                if in_deg[next_course] == 0:
                    queue.append(next_course)

        # Step 4: Check each query if the first course is a prerequisite of the second
        # Time Complexity: O(Q), where Q is the number of queries
        # Space Complexity: O(1) for the results list (excluding input/output space)
        def is_prerequisite(u: int, v: int) -> bool:
            # Closure that checks if u is a prerequisite of v using the prerequisites_map
            return u in prerequisites_map[v]

        # Process the queries and return the results
        result = [is_prerequisite(u, v) for u, v in queries]

        return result
