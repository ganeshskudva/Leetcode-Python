class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)       # Length of the input string
        cnt = 0             # Counter for consecutive characters (up to 9)
        left = 0            # Pointer to start of the current character sequence
        right = 0           # Pointer to traverse through the string
        res = []            # List to store compressed result (using list for efficient concatenation)
        
        # Loop through the string to compress it
        while right < n:
            cnt = 0         # Reset count for each new character run
            
            # Inner loop to count up to 9 consecutive identical characters
            # Time Complexity: O(n), as each character is processed only once
            while right < n and word[left] == word[right] and cnt < 9:
                right += 1
                cnt += 1
            
            # Append the count and the character to the result list
            res.append(str(cnt))    # Count as a string
            res.append(word[left])  # The character itself
            
            # Move the left pointer to the next new character in the string
            left = right

        # Join the result list into a final compressed string
        # Space Complexity: O(n) for storing the compressed output in `res`
        return ''.join(res)

# Overall Time Complexity: O(n), where n is the length of the input string `word`
#   - Each character is visited once, making the entire process linear in time.

# Overall Space Complexity: O(n)
#   - The compressed output in `res` has a maximum length of approximately 2 * n (each character
#     run could require two characters: one for the count and one for the character itself).
#   - However, this still means the space complexity is proportional to the input size.
