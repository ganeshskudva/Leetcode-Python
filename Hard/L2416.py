from collections import defaultdict

class TrieNode:
    def __init__(self):
        # Initialize 'next' as a defaultdict that will create new TrieNodes automatically when needed
        self.next = defaultdict(TrieNode)
        # Initialize 'cnt' to keep track of how many words pass through this node
        self.cnt = 0

class Solution:
    def __init__(self):
        # Initialize the root TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root  # Start at the root node
        for c in word:  # Iterate through each character in the word
            node = node.next[c]  # Move to the next node, auto-creating new TrieNode if it doesn't exist
            node.cnt += 1  # Increment the count at this node to reflect that this prefix has been visited

    def prefixCnt(self, s: str) -> int:
        node = self.root  # Start at the root node
        ans = 0  # Initialize the answer to store the sum of prefix counts
        for c in s:  # Iterate through each character in the string
            node = node.next[c]  # Move to the next node
            ans += node.cnt  # Add the count at this node to the result
        return ans  # Return the total sum of prefix counts for the given string

    def sumPrefixScores(self, words: list[str]) -> list[int]:
        N = len(words)  # Get the number of words
        # Insert all words into the Trie to build the prefix tree
        for word in words:
            self.insert(word)

        ans = [0] * N  # Initialize the result list to store prefix scores for each word
        # For each word, calculate the prefix count and store it in the result list
        for i in range(N):
            ans[i] = self.prefixCnt(words[i])  # Calculate the prefix sum for each word
        
        return ans  # Return the list of prefix scores
