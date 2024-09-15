class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # `integrals` will store the parity (even or odd) of vowel counts at each index of the string.
        # A tuple `(False, False, False, False, False)` represents that all vowels have been seen an even number of times.
        # The order of vowels in the tuple is ('a', 'i', 'u', 'e', 'o').
        integrals = [(False, False, False, False, False)]
        
        # `mapping` maps each vowel to its respective index in the `integrals` tuple.
        # This helps track which vowel has appeared an odd or even number of times.
        mapping = {
            "a": 0,
            "i": 1,
            "u": 2,
            "e": 3,
            "o": 4
        }

        # Iterate over the string to calculate the parity of vowel appearances at each index.
        for v in s:
            # Get the current parity vector of vowel appearances.
            vector = list(integrals[-1])
            
            # If the current character is a vowel, toggle its parity in the `vector`.
            if v in mapping:
                vector[mapping[v]] = not vector[mapping[v]]  # Toggle between even/odd count
            
            # Append the updated parity vector to the `integrals` list.
            integrals.append(tuple(vector))

        # `seen` will store the first occurrence of each parity vector.
        seen = {}
        
        # `res` will hold the length of the longest substring found where all vowels appear an even number of times.
        res = 0

        # Iterate through the `integrals` list to find the longest valid substring.
        for i, v in enumerate(integrals):
            if v in seen:  # If we have seen this parity vector before
                # Calculate the length of the substring and update the result if it's the longest found.
                res = max(res, i - seen[v])
            else:
                # Record the first occurrence of this parity vector.
                seen[v] = i

        # Return the length of the longest substring where all vowels appear an even number of times.
        return res

        