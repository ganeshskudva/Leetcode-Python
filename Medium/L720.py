class TrieNode:
    def __init__(self):
        # Initialize a dictionary where keys are characters and values are TrieNode instances.
        # The word property stores a string if a word ends at this node.
        self.children = defaultdict(TrieNode)
        self.word = ""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Initialize the Trie root node and result container (as a list for mutability).
        root, res = TrieNode(), [""]

        def insert(w):
            # Insert a word into the Trie.
            curr = root  # Start from the root node.
            for c in w:  # For each character in the word...
                curr = curr.children[c]  # Move to the child node corresponding to the character.
            curr.word = w  # Once the word is fully inserted, store it at the last node.

        def solve(node):
            # Depth-first search (DFS) to find the longest word.
            if node.word:  # Check if the node has a valid word (not an empty string).
                # If the current word is longer than the result word, update the result.
                if len(node.word) > len(res[0]):
                    res[0] = node.word
                # If the current word has the same length but is lexicographically smaller, update result.
                elif len(node.word) == len(res[0]) and node.word < res[0]:
                    res[0] = node.word

            # Recursively visit all children of the current node.
            for child in node.children.values():
                if child.word:  # Proceed only if the child node contains a valid word.
                    solve(child)  # Recursively apply DFS to the child node.

        # Insert all words into the Trie structure.
        for w in words:
            insert(w)

        # Perform a DFS traversal starting from the root to find the longest word.
        solve(root)

        # Return the longest word stored in the result.
        return res[0]