class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize index pointer to keep track of where to write the next compressed character.
        index = 0

        # Initialize i as the pointer to traverse the input list.
        i = 0
        while i < len(chars):
            # j will be used to find the end of a sequence of identical characters.
            j = i
            # Move j forward as long as chars[j] equals chars[i] (count identical characters).
            while j < len(chars) and chars[i] == chars[j]:
                j += 1

            # Update chars at the current index with the current character.
            chars[index] = chars[i]
            index += 1

            # Calculate the frequency of the current character.
            freq = j - i
            # If the frequency is greater than 1, convert the frequency to a string
            # and write each digit to the chars array.
            if freq > 1:
                for digit in str(freq):
                    chars[index] = digit
                    index += 1

            # Move i to the next group of characters (i.e., to the position of j).
            i = j

        # Return the final length of the compressed string (the value of index).
        return index

# Time Complexity (TC):
# 1. The outer loop traverses the list 'chars' once, so the loop runs O(n) times where 'n' is the number of characters in 'chars'.
# 2. The inner loop that counts identical characters also moves 'j' pointer across the list but does not exceed O(n) in total, since both 'i' and 'j' traverse the list once.
# 3. Converting the frequency to a string and updating the array for each frequency involves O(log(freq)) operations, but this happens only when there are runs of repeated characters.
# Therefore, the overall time complexity is O(n), where 'n' is the number of characters in the 'chars' list.

# Space Complexity (SC):
# 1. The only extra space used is for a few variables (like 'index', 'i', 'j', and 'freq') and a temporary string for the frequency digits.
# 2. No additional data structures of significant size are used, and the compression is done in-place.
# Therefore, the space complexity is O(1) since the algorithm only uses a constant amount of extra space.
