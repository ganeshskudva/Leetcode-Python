## BFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # vis: a set to track visited nodes (courses we've completed)
        # deg: an array that stores the in-degree (number of prerequisites) for each course
        # mp: a dictionary where each key points to a list of courses that depend on that key course
        # Time Complexity: O(V + E), Space Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites
        vis, deg, mp = set(), [0] * numCourses, defaultdict(list)

        # Step 1: Build the graph and calculate the in-degrees of each course
        # Time Complexity: O(E), where E is the number of prerequisites
        # Space Complexity: O(V + E) for storing the adjacency list and in-degree array
        for src, dep in prerequisites:
            mp[dep].append(src)  # dep -> src (src depends on dep)
            deg[src] += 1  # Increase the in-degree of the course that depends on another

        # Step 2: Initialize the queue with courses that have 0 prerequisites (in-degree 0)
        # Time Complexity: O(V), where V is the number of courses
        # Space Complexity: O(V) for storing the queue
        q = deque([i for i in range(numCourses) if not deg[i]])

        # Step 3: Process the queue using BFS (Topological Sort)
        # Time Complexity: O(V + E), where V is the number of courses and E is the number of edges (prerequisites)
        # Space Complexity: O(V + E), since we store the visited nodes and the modified in-degree graph
        while q:
            node = q.popleft()  # Get a course with 0 prerequisites
            if node in vis:
                continue  # Skip if we've already processed this node
            vis.add(node)  # Mark the course as visited (completed)
            for dep in mp[node]:  # Go through all courses dependent on this course
                deg[dep] -= 1  # Decrease the in-degree of dependent courses
                if not deg[dep]:  # If the in-degree becomes 0, add the course to the queue
                    q.append(dep)

        # Step 4: Check if we've completed all the courses
        # If the number of visited nodes equals the total number of courses, return True
        return len(vis) == numCourses

# Overall Time Complexity (TC):
# - O(V + E), where V is the number of courses (vertices), and E is the number of prerequisites (edges).
#   - O(V) to initialize the degree array and queue.
#   - O(E) to build the adjacency list (graph) and reduce in-degrees.
#   - The BFS traversal processes each vertex (course) and each edge (prerequisite) at most once.

# Overall Space Complexity (SC):
# - O(V + E), where V is the number of courses and E is the number of prerequisites.
#   - O(V) for the degree array, queue, and visited set.
#   - O(E) for storing the adjacency list in the dictionary.


## DFS


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # vis: a set to track visited nodes (courses we've completed)
        # deg: an array that stores the in-degree (number of prerequisites) for each course
        # mp: a dictionary where each key points to a list of courses that depend on that key course
        # Time Complexity: O(V + E), Space Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites
        vis, deg, mp = set(), [0] * numCourses, defaultdict(list)
        
        # Step 1: Build the graph and calculate the in-degrees of each course
        # Time Complexity: O(E), where E is the number of prerequisites (edges)
        # Space Complexity: O(V + E), for storing the adjacency list and in-degree array
        for src, dep in prerequisites:
            mp[dep].append(src)  # dep -> src (src depends on dep)
            deg[src] += 1  # Increase the in-degree of the course that depends on another
        
        # Recursive helper function to perform DFS and decrease in-degrees
        # Time Complexity per node: O(V + E) in total since we process each node and edge once
        # Space Complexity per node: O(V + E) for recursion depth and in-degree modification
        def solve(node):
            if node in vis:
                return  # If the course has been visited, skip processing it again
            vis.add(node)  # Mark the course as visited (completed)
            for dep in mp[node]:  # Go through all courses dependent on this course
                deg[dep] -= 1  # Decrease the in-degree of dependent courses
                if not deg[dep]:  # If the in-degree becomes 0, solve that course recursively
                    solve(dep)

        # Step 2: Start DFS from all nodes that have no prerequisites (in-degree == 0)
        # Time Complexity: O(V), where V is the number of courses
        # Space Complexity: O(V) for storing the visited set and processing each course
        for i in range(len(deg)):
            if not deg[i]:  # If a course has no prerequisites, start solving it
                solve(i)
        
        # Step 3: Check if we've visited all the courses
        # Time Complexity: O(1) since it checks the length of the set
        # Space Complexity: O(1) since it returns a boolean
        return len(vis) == numCourses

# Overall Time Complexity (TC):
# O(V + E), where V is the number of courses and E is the number of prerequisites (edges).
# - We build the graph in O(E).
# - Each course (node) is processed once, and for each course, we visit its edges (prerequisites), so this leads to O(V + E).

# Overall Space Complexity (SC):
# O(V + E), where V is the number of courses and E is the number of prerequisites.
# - O(V) for the degree array, visited set, and function recursion.
# - O(E) for storing the adjacency list of prerequisites.
