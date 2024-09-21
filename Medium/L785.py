class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # n is the number of nodes in the graph
        n = len(graph)
        
        # colors array keeps track of the color assigned to each node.
        # 0 means uncolored, 1 and -1 represent the two different colors.
        colors = [0] * n
        
        # Helper function to determine if we can color the graph starting from a node.
        def is_valid(color, node):
            # If the node is already colored
            if colors[node] != 0:
                # Check if the current color is the same as the color we want to assign.
                return colors[node] == color
            
            # Assign the color to the current node
            colors[node] = color
            
            # Recursively check all adjacent nodes (neighbors)
            for nei in graph[node]:
                # Try to color the neighboring node with the opposite color (-color)
                if not is_valid(-color, nei):
                    return False  # If it leads to a conflict, the graph is not bipartite
            return True  # If all neighbors are valid, return True
        
        # Main loop to check each node (in case the graph is disconnected)
        for i in range(n):
            # If a node is not yet colored, try to color it with color 1.
            # If it cannot be colored properly, the graph is not bipartite.
            if colors[i] == 0 and not is_valid(1, i):
                return False
        
        # If we can color the entire graph without conflict, it is bipartite
        return True
