class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = [''] * len(queries)

        # Helper to strip vowels (replace them with #)
        def strip_vowels(word):
            return word.translate(str.maketrans("aeiouAEIOU", "##########"))

        # If wordlist or queries is empty, return the initialized empty result
        if not wordlist or not queries:
            return res

        # Sets and dictionaries for exact match, case-insensitive match, and vowel-insensitive match
        words = set(wordlist)
        capitals = {}
        vowels = {}

        # Preprocess the wordlist
        for w in wordlist:
            lower = w.lower()
            vowel_stripped = strip_vowels(lower)

            # Capital-sensitive dictionary
            if lower not in capitals:
                capitals[lower] = w

            # Vowel-insensitive dictionary
            if vowel_stripped not in vowels:
                vowels[vowel_stripped] = w

        # Process each query
        for i, query in enumerate(queries):
            if query in words:
                res[i] = query
                continue

            lower = query.lower()
            vowel_stripped = strip_vowels(lower)

            # Check for case-insensitive match
            if lower in capitals:
                res[i] = capitals[lower]
            # Check for vowel-insensitive match
            elif vowel_stripped in vowels:
                res[i] = vowels[vowel_stripped]

        return res


# Time Complexity (TC):
# Preprocessing the wordlist: O(m * l), where `m` is the number of words in the wordlist, and `l` is the average word length.
# Processing each query: O(n * l), where `n` is the number of queries, and `l` is the average query length.
# The total time complexity is O(m * l + n * l).

# Space Complexity (SC):
# The space used by the dictionaries for exact, case-insensitive, and vowel-insensitive matching is O(m * l), where `m` is the number of words and `l` is the average length of the words.
# The space for the result list is O(n), where `n` is the number of queries.
# The total space complexity is O(m * l + n).