class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_str = list(str(n))  # Convert the integer to a list of its digits
        i = len(n_str) - 2  # Start from the second last digit

        # Find the first digit that is smaller than the digit next to it, scanning from right to left
        while i >= 0 and n_str[i] >= n_str[i + 1]:
            i -= 1

        # If no such digit is found, return -1 (this means the number is the largest possible permutation)
        if i < 0:
            return -1

        # Find the smallest digit on the right side that is larger than n_str[i]
        j = len(n_str) - 1
        while n_str[j] <= n_str[i]:
            j -= 1

        # Swap the found digits
        n_str[i], n_str[j] = n_str[j], n_str[i]

        # Reverse the digits after position i to get the smallest possible permutation
        n_str[i + 1:] = n_str[i + 1:][::-1]

        # Convert the list of characters back to an integer
        result = int(''.join(n_str))

        # Check if the result fits within the 32-bit signed integer range
        if result > 2**31 - 1:
            return -1

        return result