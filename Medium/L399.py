class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph, res = defaultdict(list), [0.0] * len(queries)

        def build_graph():
            for i in range(len(equations)):
                start, dest = equations[i][0], equations[i][1]
                graph[start].append((dest, values[i]))
                graph[dest].append((start, 1/values[i]))

        def solve(start, end, value, vis=None):
            if vis is None:
                vis = set()
            if start not in graph or end not in graph:
                return -1.0
            if start in vis:
                return -1.0

            if start == end:
                return value

            vis.add(start)
            for i in range(len(graph[start])):
                weight = solve(graph[start][i][0], end, value * graph[start][i][1], vis)
                if weight != -1.0:
                    return weight

            return -1.0

        build_graph()
        for i in range(len(queries)):
            res[i] = solve(queries[i][0], queries[i][1], 1.0)

        return res
