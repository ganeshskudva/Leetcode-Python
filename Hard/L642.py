class TrieNode:
    def __init__(self):
        # Initialize children map and counts map
        # `children` is a dictionary that maps each character to its corresponding TrieNode
        self.children = defaultdict(TrieNode)
        # `counts` keeps track of the frequency of each sentence that passes through this node
        self.counts = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences, times):
        # Initialize the trie root and the current prefix being typed (as a list of characters)
        self.root = TrieNode()
        self.prefix = []  # Prefix is stored as a list of characters

        # Insert the initial sentences into the trie with their counts
        for i in range(len(sentences)):
            self._add(sentences[i], times[i])

    def _add(self, s, count):
        """
        Add a sentence `s` into the trie with a given count (frequency of occurrence).
        The sentence is added character by character, updating the `counts` for each node.
        """
        curr = self.root
        for c in s:
            curr = curr.children[c]  # Move to the next node in the trie
            curr.counts[s] += count  # Update the count of the sentence in this node

    def input(self, c):
        """
        Process each character input and return the top 3 sentences that match the current prefix.
        If `c` is '#', add the current prefix to the trie and reset the prefix.
        """
        if c == '#':
            # When '#' is entered, it signals the end of a sentence, so add the current sentence to the trie.
            self._add(''.join(self.prefix), 1)  # Join prefix list to form the complete sentence
            self.prefix = []  # Reset the prefix list
            return []  # Return an empty list after adding the sentence

        # Append the current character to the prefix list
        self.prefix.append(c)
        curr = self.root

        # Traverse the trie based on the current prefix
        for char in self.prefix:
            if char not in curr.children:
                return []  # If no matching node, return an empty list (no sentences match the prefix)
            curr = curr.children[char]

        # Use a priority queue (min-heap) to collect the top 3 suggestions
        pq = []
        for s, count in curr.counts.items():
            # Push sentence `s` and its negative count (for max-heap behavior) into the heap
            heapq.heappush(pq, (-count, s))

        # Extract the top 3 results from the priority queue
        res, req = [], 3
        while pq and req:
            res.append(heapq.heappop(pq)[1])  # Append the sentence (second element of tuple) to the result
            req -= 1  # Decrease the number of required sentences

        return res