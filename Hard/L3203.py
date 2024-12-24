from typing import List, Tuple

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter_calculator():
            """
            Closure to calculate the diameter of a graph.
            """
            def farthest(graph: List[List[int]], start: int) -> Tuple[int, int]:
                """
                Finds the farthest node from the start node and its distance.
                TC: O(V + E), where V is the number of vertices and E is the number of edges.
                SC: O(V) for the `seen` list.
                """
                n = len(graph)
                level = [start]
                seen = [0] * n
                seen[start] = 1
                farthest_node = start
                max_distance = -1
                for node in level:
                    for neighbor in graph[node]:
                        if not seen[neighbor]:
                            seen[neighbor] = seen[node] + 1
                            level.append(neighbor)
                            if seen[neighbor] > max_distance:
                                farthest_node = neighbor
                                max_distance = seen[neighbor]
                return farthest_node, max_distance - 1

            def diameter(edges: List[List[int]]) -> int:
                """
                Calculates the diameter of a tree represented by edges.
                TC: O(V + E), SC: O(V).
                """
                if not edges:
                    return 0
                n = len(edges) + 1
                graph = [[] for _ in range(n)]
                for u, v in edges:
                    graph[u].append(v)
                    graph[v].append(u)
                node1, _ = farthest(graph, 0)
                _, d = farthest(graph, node1)
                return d

            return diameter

        # Initialize the closure for diameter calculation
        calculate_diameter = diameter_calculator()

        # Compute the diameters for both edge sets
        d1 = calculate_diameter(edges1)
        d2 = calculate_diameter(edges2)

        # Merge logic to compute the minimum diameter after merging
        # TC: O(V + E) for each graph's traversal, SC: O(V) for auxiliary structures.
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)

"""
Overall Time Complexity (TC):
- O(V1 + E1 + V2 + E2), where V1 and E1 are the vertices and edges in edges1, and V2 and E2 are the vertices and edges in edges2.

Overall Space Complexity (SC):
- O(V1 + V2) for the auxiliary `seen` lists and graph representations.
"""