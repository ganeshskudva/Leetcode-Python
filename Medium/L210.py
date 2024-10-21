## BFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # res: list to store the course order
        # vis: set to track visited courses (courses that have been added to the order)
        # in_degree: list to track how many prerequisites each course has (in-degree)
        # q: queue to store courses with no remaining prerequisites (in-degree 0)
        # adj: adjacency list to represent the graph (course dependencies)
        res, vis, in_degree, q, adj = [], set(), [0] * numCourses, deque(), defaultdict(list)

        # Step 1: Build the graph and calculate the in-degrees for each course
        # Time Complexity: O(E), where E is the number of prerequisites (edges)
        # Space Complexity: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges)
        for p in prerequisites:
            in_degree[p[0]] += 1  # Increment the in-degree of the course that depends on another
            adj[p[1]].append(p[0])  # Add the dependency relationship to the adjacency list

        # Step 2: Initialize the queue with courses that have no prerequisites (in-degree == 0)
        # Time Complexity: O(V), where V is the number of courses (vertices)
        # Space Complexity: O(V) for storing the queue
        for i in range(numCourses):
            if not in_degree[i]:  # If the course has no prerequisites, add it to the queue
                q.append(i)

        # Step 3: Process the queue using BFS (Topological Sort)
        # Time Complexity: O(V + E), where V is the number of courses (vertices) and E is the number of prerequisites (edges)
        # Space Complexity: O(V + E), for storing the visited set, adjacency list, and the in-degree array
        while q:
            size = len(q)
            for _ in range(size):
                n = q.popleft()  # Get a course with no remaining prerequisites
                if n in vis:  # If already processed, skip it
                    continue
                res.append(n)  # Add the course to the result list (order)
                vis.add(n)  # Mark the course as visited

                # Go through all courses dependent on the current course
                for c in adj[n]:
                    in_degree[c] -= 1  # Decrease the in-degree of dependent courses
                    if not in_degree[c]:  # If the in-degree becomes 0, add the course to the queue
                        q.append(c)

        # Step 4: If all courses have been processed, return the result; otherwise, return an empty list
        # Time Complexity: O(1) for the final check
        # Space Complexity: O(1) since the result list is already computed
        return res if numCourses == len(vis) else []

# Overall Time Complexity (TC):
# O(V + E), where V is the number of courses and E is the number of prerequisites.
# - Building the in-degree array and adjacency list takes O(E).
# - The BFS traversal processes each course (V) and its edges (E), resulting in O(V + E).

# Overall Space Complexity (SC):
# O(V + E), where V is the number of courses and E is the number of prerequisites.
# - O(V) for the in-degree array, result list, visited set, and queue.
# - O(E) for the adjacency list representing the prerequisites.

