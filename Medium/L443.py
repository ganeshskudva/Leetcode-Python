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