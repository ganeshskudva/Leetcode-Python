class Solution:
    def minDays(self, grid):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def count_island(grid):
            r, c = len(grid), len(grid[0])
            visited = [[False] * c for _ in range(r)]
            cnt = 0
            
            def dfs(r, c):
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or visited[r][c] or grid[r][c] != 1:
                    return
                visited[r][c] = True
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)
            
            for i in range(r):
                for j in range(c):
                    if not visited[i][j] and grid[i][j] == 1:
                        dfs(i, j)
                        cnt += 1
            return cnt

        r, c = len(grid), len(grid[0])
        cnt = count_island(grid)
        if cnt == 0 or cnt > 1:
            return 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    cnt = count_island(grid)
                    grid[i][j] = 1
                    if cnt == 0 or cnt > 1:
                        return 1
        return 2
