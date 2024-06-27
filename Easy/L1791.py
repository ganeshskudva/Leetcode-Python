class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        for src, dest in edges:
            graph[src] += 1
            graph[dest] += 1
        
        for k, v in graph.items():
            if v == len(edges):
                return k
        
        return -1
