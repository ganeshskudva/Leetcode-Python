class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []  # Using a list to build the result string for efficiency
        curr_a = curr_b = curr_c = 0  # Counters for consecutive occurrences of 'a', 'b', and 'c'
        max_len = a + b + c  # The total possible length of the result string

        # The loop continues until we build the longest possible diverse string
        while len(result) < max_len:
            # Condition to add 'a' to the result
            if (curr_a != 2 and a >= b and a >= c) or (a > 0 and (curr_b == 2 or curr_c == 2)):
                result.append('a')  # Add 'a' to the result
                curr_a += 1  # Increment the 'a' counter
                curr_b = curr_c = 0  # Reset 'b' and 'c' counters
                a -= 1  # Decrease the count of remaining 'a's

            # Condition to add 'b' to the result
            elif (curr_b != 2 and b >= a and b >= c) or (b > 0 and (curr_a == 2 or curr_c == 2)):
                result.append('b')  # Add 'b' to the result
                curr_b += 1  # Increment the 'b' counter
                curr_a = curr_c = 0  # Reset 'a' and 'c' counters
                b -= 1  # Decrease the count of remaining 'b's

            # Condition to add 'c' to the result
            elif (curr_c != 2 and c >= a and c >= b) or (c > 0 and (curr_a == 2 or curr_b == 2)):
                result.append('c')  # Add 'c' to the result
                curr_c += 1  # Increment the 'c' counter
                curr_a = curr_b = 0  # Reset 'a' and 'b' counters
                c -= 1  # Decrease the count of remaining 'c's

            # If no valid character can be appended, we break the loop
            else:
                break

        # Join the list of characters into a string and return
        return ''.join(result)

# Time Complexity (TC):
# The loop runs at most a + b + c times, which is the length of the resulting string.
# Each operation inside the loop (comparison, appending, decrementing counts) is O(1).
# Therefore, the overall time complexity is O(a + b + c).

# Space Complexity (SC):
# The space used is mainly for storing the result list, which can grow to a length of at most a + b + c.
# Therefore, the space complexity is O(a + b + c) for the result list.