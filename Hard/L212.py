from typing import List
import collections

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Result set to store unique words found on the board
        res = set()
        # Initialize Trie and insert all words into it
        trie = Trie()
        m, n = len(board), len(board[0])  # Dimensions of the board
        node = trie.root
        
        # Insert each word into the Trie
        for w in words:
            trie.insert(w)

        # Check if cell (x, y) is within board boundaries
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        # DFS function to explore the board and find words
        def solve(i, j, path, trie_node):
            # If the Trie node represents a complete word, add it to results
            if trie_node.is_word:
                res.add(path)
                trie_node.is_word = False  # Avoid duplicate words in the result set

            # Boundary and validity check
            if not is_valid(i, j):
                return

            # Retrieve the character from the board and the corresponding Trie node
            tmp = board[i][j]
            trie_node = trie_node.children.get(tmp)
            if not trie_node:  # Stop if character does not match Trie path
                return

            # Mark the cell as visited by setting it to a placeholder character
            board[i][j] = "#"
            # Define directions for exploration: right, down, left, up
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            # Explore in all four directions
            for x, y in dirs:
                solve(i + x, j + y, path + tmp, trie_node)
            # Restore the cell's original value for backtracking
            board[i][j] = tmp

        # Start DFS from each cell in the board
        for i in range(m):
            for j in range(n):
                solve(i, j, "", node)
        
        # Convert set of results to list before returning
        return list(res)

# Time Complexity (TC) and Space Complexity (SC) of the Solution:
# 
# - TC for building the Trie: O(K), where K is the total number of characters in all words.
# - TC for DFS traversal: O(M * N * 4^L), where:
#     - M and N are the dimensions of the board.
#     - L is the length of the longest word.
#     - Each cell may branch in 4 directions, giving a branching factor of 4^L.
# - Overall TC: O(K + M * N * 4^L)
# 
# - SC for Trie storage: O(K), as it stores each character in all words.
# - SC for DFS recursion stack: O(L), with L being the longest word length.
# - SC for visited cells: No extra space required as the board is temporarily modified.
# - SC for results storage: O(W), where W is the number of unique words found.
# - Overall SC: O(K + L + W)

class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = collections.defaultdict(TrieNode)
        # Boolean flag to mark the end of a word
        self.is_word = False

class Trie:
    def __init__(self):
        # Root node of the Trie
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        # Mark the last node as the end of a word
        node.is_word = True
