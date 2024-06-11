class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n, rotten_cnt, fresh_cnt = len(grid), len(grid[0]), 0, 0
        q, vis, res = deque(), set(), 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    rotten_cnt += 1
                    q.append((i, j))

        if not fresh_cnt:
            return 0

        if not q or len(q) == m*n:
            return -1

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        def bfs():
            cnt = 0
            while q:
                size = len(q)
                for i in range(size):
                    n = q.popleft()

                    grid[n[0]][n[1]] = 2
                    vis.add((n[0], n[1]))
                    for d in dirs:
                        new_x, new_y = n[0] + d[0], n[1] + d[1]
                        if is_valid(new_x, new_y) and \
                                (new_x, new_y) not in vis:
                            vis.add((new_x, new_y))
                            q.append((new_x, new_y))
                cnt += 1

            return cnt

        res = bfs()

        return res - 1 if (rotten_cnt + fresh_cnt) == len(vis) else -1
