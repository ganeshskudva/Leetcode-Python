class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create sets for BFS from both directions
        begin_set, end_set, vis = {beginWord}, {endWord}, set()
        mp = set(wordList)

        # Early return if `endWord` is not in the word list
        if endWord not in mp:
            return 0
        
        # Length of the transformation sequence
        length = 1
        
        # Bi-directional BFS loop
        while begin_set and end_set:
            # Always expand the smaller set for better performance
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            tmp = set()  # Temporary set for the next level of BFS
            
            # Explore each word in `begin_set`
            for s in begin_set:
                for i in range(len(s)):
                    # Try changing each character in the word (a-z)
                    for ch in range(26):
                        # Create the new word by changing one character at index `i`
                        tgt = s[:i] + chr(ch + ord('a')) + s[i + 1:]

                        # If the transformed word is in `end_set`, transformation is complete
                        if tgt in end_set:
                            return length + 1

                        # If the transformed word is in the word list and not visited
                        if tgt not in vis and tgt in mp:
                            vis.add(tgt)  # Mark the word as visited
                            tmp.add(tgt)  # Add the word to the next BFS level

            # Move to the next BFS level
            begin_set = tmp
            length += 1

        # If no transformation sequence is found, return 0
        return 0

        