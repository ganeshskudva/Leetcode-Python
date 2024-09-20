class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Define a closure to calculate the KMP table (getTable equivalent)
        def get_table(s: str):
            # Initialize the table with zeros
            table = [0] * len(s)
            # Pointer that points to the matched character in the prefix part
            index = 0
            # Skip the first character, as we don't match a string with itself
            for i in range(1, len(s)):
                if s[index] == s[i]:
                    # We can extend the match in the prefix and postfix
                    table[i] = table[i - 1] + 1
                    index += 1
                else:
                    # Match failed, try to match a shorter substring
                    index = table[i - 1]
                    # Shorten the match string length until we revert to the beginning of match (index 0)
                    while index > 0 and s[index] != s[i]:
                        index = table[index - 1]
                    # If characters match, extend the match
                    if s[index] == s[i]:
                        index += 1
                    # Update the table with the length of the current prefix
                    table[i] = index
            return table

        # Combine the input string, a special character (#) and the reverse of the string
        temp = s + "#" + s[::-1]
        # Get the KMP table using the closure
        table = get_table(temp)

        # The longest palindrome substring starts from the beginning of `s`
        # Add the reverse of the remaining part of `s` to the front
        return s[table[-1]:][::-1] + s