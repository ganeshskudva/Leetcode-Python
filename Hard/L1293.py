class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n, res, q, vis = len(grid), len(grid[0]), 0, deque(), set()
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        def is_boundary(r, c):
            return r == m - 1 and c == n - 1

        vis.add((0, 0, 0))
        q.append((0, 0, 0))
        while q:
            size = len(q)
            for _ in range(size):
                row, col, curr_k = q.popleft()
                if is_boundary(row, col):
                    return res
                for dx, dy in dirs:
                    next_row, next_col, next_k = row + dx, col + dy, curr_k
                    if is_valid(next_row, next_col):
                        if grid[next_row][next_col] == 1:
                            next_k += 1
                        if next_k <= k and (next_row, next_col, next_k) not in vis:
                            vis.add((next_row, next_col, next_k))
                            q.append((next_row, next_col, next_k))
            res += 1

        return -1