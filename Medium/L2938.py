class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        Given a binary string 's' composed of '0's and '1's, this function calculates the minimum number of swaps
        needed to move all '1's to the right of all '0's. A 'swap' is defined as swapping adjacent characters.

        The algorithm counts the number of '1's (black) encountered as it iterates through the string. Each time a '0'
        is encountered, it means all the '1's seen so far would need to swap with this '0' to move to the right.

        Parameters:
        s (str): The input binary string of '0's and '1's.

        Returns:
        int: The minimum number of adjacent swaps needed.

        TC: O(n) where n is the length of the string 's'.
        - We iterate through the string once, performing constant time operations for each character.

        SC: O(1) (constant space).
        - Only a few variables (swap, black) are used, regardless of the input size.
        """

        swap, black = 0, 0  # Initialize swap count and count of '1's (black) seen so far

        for c in s:
            if c == "0":  # If the character is '0', we calculate how many swaps are needed with '1's seen so far
                swap += black  # Every '1' seen before this '0' needs to swap with it
            else:
                black += 1  # Count the number of '1's encountered

        return swap  # Return the total number of swaps needed
