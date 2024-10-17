class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert num to a list of digits and create a dictionary to store the last occurrence of each digit
        # TC: O(n) where n is the number of digits in the input number
        # SC: O(n) for storing the list of digits
        mp, digits = defaultdict(int), list(str(num))

        # Store the last occurrence of each digit in the dictionary
        # TC: O(n) for iterating over each digit to store its last occurrence
        # SC: O(1) for the dictionary, since it stores only 10 digits (0-9)
        for i, v in enumerate(digits):
            mp[ord(v) - ord('0')] = i

        # Iterate over the digits to find the first digit that can be swapped for a larger one
        # TC: O(n) for iterating over each digit
        for i in range(len(digits)):
            # Check if there's a larger digit we can swap with, starting from 9 down to the current digit
            # TC: O(1), since it only checks up to 9 possible digits
            for k in range(9, ord(digits[i]) - ord('0'), -1):
                # If a larger digit exists and its position is after the current digit
                if mp[k] > i:
                    # Swap the digits
                    digits[i], digits[mp[k]] = digits[mp[k]], digits[i]
                    # Return the integer value after swapping
                    # TC: O(n) to join the digits and convert them back to an integer
                    return int(''.join(digits))

        # If no swap is possible, return the original number
        # TC: O(1), constant time return
        return num

# Overall Time Complexity (TC): 
# - O(n) for storing the last occurrence of each digit
# - O(n) for iterating over the digits to find a possible swap
# - O(n) to convert the digits back to an integer after the swap
# Total TC: O(n)

# Overall Space Complexity (SC): 
# - O(n) for the list of digits
# - O(1) for the dictionary storing the last occurrence of digits (constant size for 0-9)
# Total SC: O(n)
