class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        trie = Trie()
        m, n = len(board), len(board[0])
        node = trie.root
        for w in words:
            trie.insert(w)

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def solve(i, j, path, trie_node):
            if trie_node.is_word:
                res.add(path)
                trie_node.isWord = False

            if not is_valid(i, j):
                return
            tmp = board[i][j]
            trie_node = trie_node.children.get(tmp)
            if not trie_node:
                return
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            board[i][j] = "#"
            for x, y in dirs:
                solve(i + x, j + y, path + tmp, trie_node)
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                solve(i, j, "", node)
        return list(res)

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True
