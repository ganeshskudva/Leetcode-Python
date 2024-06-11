class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not len(rooms[0]):
            return
        inf = 2147483647
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q, m, n = deque(), len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:
                    q.append((i, j))

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and rooms[x][y] == inf

        while q:
            row, col = q.popleft()
            dist = rooms[row][col] + 1
            for d in dirs:
                new_x, new_y = row + d[0], col + d[1]
                if is_valid(new_x, new_y):
                    rooms[new_x][new_y] = dist
                    q.append((new_x, new_y))
