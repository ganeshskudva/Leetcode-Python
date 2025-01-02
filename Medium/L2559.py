class Solution:
    def vowelStrings(self, words, queries):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)

        # Build the prefix array in O(n)
        prefix = [0] * (n + 1)
        for i, word in enumerate(words):
            prefix[i + 1] = prefix[i] + (word[0] in vowels and word[-1] in vowels)

        # Answer the queries in O(q)
        return [prefix[end + 1] - prefix[start] for start, end in queries]

# Time Complexity (TC):
# - Prefix array construction: O(n), where n is the length of the `words` list.
# - Query processing: O(q), where q is the number of queries.
# - Overall: O(n + q)

# Space Complexity (SC):
# - Prefix array: O(n) for storing cumulative counts.
# - Total: O(n)
