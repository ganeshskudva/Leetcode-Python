from collections import defaultdict, deque

def alien_order(words):
    # Step 1: Build the graph and maintain visitation state
    adj = defaultdict(list)  # Adjacency list to represent the graph
    visited = {}  # To track visit states: -1 = doesn't exist, 0 = unvisited, 1 = visiting, 2 = visited
    
    def build_graph(words):
        # Initialize visited state (-1 means the character doesn't exist in any word)
        for word in words:
            for char in word:
                visited[char] = 0  # Mark all characters as initially unvisited

        # Step 2: Create the adjacency list
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # There is an edge from w1[j] -> w2[j] in the alien dictionary
                    adj[w1[j]].append(w2[j])
                    break
            # Case where w1 is a prefix of w2 but longer: invalid order
            else:
                if len(w1) > len(w2):
                    return False  # Invalid lexicographical order
        return True

    # Step 3: Perform DFS to detect cycles and create the topological sort
    def dfs(node, result):
        visited[node] = 1  # Mark as visiting
        for neighbor in adj[node]:
            if visited[neighbor] == 1:  # Found a cycle
                return False
            if visited[neighbor] == 0:  # Not visited yet
                if not dfs(neighbor, result):
                    return False
        visited[node] = 2  # Mark as visited
        result.append(node)  # Append to the result (reverse order due to DFS)
        return True
    
    # Step 4: Use a closure to combine the graph-building and DFS logic
    def alien_dictionary():
        # If graph is invalid during construction, return ""
        if not build_graph(words):
            return ""
        
        result = []  # Holds the topologically sorted order
        for node in visited:
            if visited[node] == 0:  # Unvisited node
                if not dfs(node, result):
                    return ""  # Cycle found, invalid order
        return "".join(reversed(result))  # Reverse result to get the correct order
    
    return alien_dictionary()

# Time Complexity (TC):
# - Building the graph: Each word comparison takes at most O(k) where k is the length of the shorter word,
#   and there are n-1 comparisons for n words. Therefore, building the graph takes O(n * k).
# - DFS traversal: In the worst case, we visit each character (node) and its neighbors (edges).
#   Hence, the DFS takes O(V + E), where V is the number of unique characters and E is the number of edges.
# - Overall TC: O(n * k + V + E), where n is the number of words, k is the average word length,
#   V is the number of unique characters (nodes), and E is the number of edges (adjacency list size).

# Space Complexity (SC):
# - The adjacency list requires O(V + E) space to store the graph.
# - The visited dictionary uses O(V) space to track the state of each node.
# - The recursion stack for DFS can go as deep as O(V) in the worst case.
# - Overall SC: O(V + E) for graph storage and DFS recursion.
