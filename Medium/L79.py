class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(word) == 0:
            return False

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(board), len(board[0])
        vis = set()

        def is_valid(x, y, ch):
            m, n = len(board), len(board[0])

            return 0 <= x < m and 0 <= y < n and ord(board[x][y]) == ord(ch)

        def solve(i, j, index):
            if index == len(word):
                return True

            if not is_valid(i, j, word[index]):
                return False

            if (i, j) in vis:
                return False

            vis.add((i, j))
            found = False
            for d in dirs:
                found = found or solve(i + d[0], j + d[1], index + 1)
            vis.remove((i, j))

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if solve(i, j, 0):
                        return True

        return False
