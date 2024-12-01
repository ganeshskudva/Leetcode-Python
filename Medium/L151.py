class Solution:
    def reverseWords(self, s: str) -> str:
        res, temp = [], []  # `res` will store the words, `temp` is a temporary list for building each word
        
        for c in s:  # Iterate through each character in the string
            if c != ' ':  # If the character is not a space, add it to the current word (`temp`)
                temp.append(c)
            elif temp:  # If a space is encountered and `temp` is not empty (end of a word)
                res.append(''.join(temp))  # Join the characters in `temp` to form a word and add it to `res`
                temp = []  # Reset `temp` for the next word
        
        if temp:  # After the loop, if `temp` contains a word, add it to `res`
            res.append(''.join(temp))
        
        return ' '.join(res[::-1])  # Reverse the order of words in `res` and join them with a single space

# Time Complexity (TC):
# 1. Iterating over the string: O(n), where n is the length of the string.
#    - Each character is processed exactly once.
# 2. Reversing the list of words: O(k), where k is the number of words.
#    - Since k ≤ n, this simplifies to O(n).
# 3. Joining the words into a final string: O(n), as all characters are processed during the join.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. Temporary list `temp`: At most O(m), where m is the length of the longest word.
# 2. List `res`: Stores all words, requiring O(k) space, where k is the total number of characters across all words (≤ n).
# 3. Final reversed string: Requires O(n) space to store the result.
# Overall SC: O(n), as the space is dominated by the storage for the words and the final result.


class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by whitespace into a list of words
        # This handles multiple spaces by ignoring empty segments
        arr = s.split()  # Splitting is O(n), where n is the length of the string
        
        # Step 2: Reverse the list of words in-place
        arr.reverse()  # Reversing the list is O(k), where k is the number of words
        
        # Step 3: Join the reversed list of words into a single string
        # Each word is joined with a space, which processes all characters
        return ' '.join(arr)  # Joining is O(n), as all characters are processed

# Time Complexity (TC):
# 1. Splitting the string into words: O(n), where n is the length of the string.
#    - Each character is processed once during splitting.
# 2. Reversing the list of words: O(k), where k is the number of words.
#    - Since k ≤ n (the total length of the string), this simplifies to O(n).
# 3. Joining the words into a final string: O(n), as it processes all characters once.
# Overall TC: O(n).

# Space Complexity (SC):
# 1. List `arr`: O(k), where k is the number of words. The total space required for the list is proportional to the string length, so O(n).
# 2. Final result string: O(n), as it requires space for all characters in the string.
# Overall SC: O(n).
