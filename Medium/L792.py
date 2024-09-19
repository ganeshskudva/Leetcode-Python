class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Initialize result counter `res` to count the number of matching subsequences
        # Initialize `waiting` as a defaultdict where the key is the character in `s`
        # and the value is a list of words that are "waiting" to match with that character
        res, waiting = 0, defaultdict(list)
        
        # For each word in `words`, add it to the waiting dictionary under the key of its first character
        # This means that the word is "waiting" for its first character to be matched in the string `s`
        for w in words:
            waiting[w[0]].append(w)
        
        # Iterate through each character `c` in the string `s`
        for c in s:
            # Get the list of words that were waiting for the current character `c` and reset the waiting list for `c`
            advance, waiting[c] = waiting[c], []
            
            # For each word that was waiting for the character `c`
            for a in advance:
                # Remove the first character (which was just matched) from the word
                a = a[1:]
                
                # If the word is now empty, it means all characters in the word have been matched in sequence
                if not a:
                    res += 1  # Increment the result counter
                else:
                    # If the word still has more characters, add it back to the waiting list
                    # under the key of the next character it is waiting for
                    waiting[a[0]].append(a)
        
        # Return the total count of words that were subsequences of `s`
        return res
