from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Valid digit pairs for strobogrammatic numbers
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

        def helper(cur_len: int) -> List[str]:
            # Base cases
            if cur_len == 0:  # If no digits left, return an empty string as a base case
                return [""]
            if cur_len == 1:  # If only one digit left, return valid single-digit strobogrammatic numbers
                return ["0", "1", "8"]

            # Recursive call to get all strobogrammatic numbers for smaller length
            sub = helper(cur_len - 2)
            result = []

            # Iterate through each smaller-length number and wrap it with valid pairs
            for s in sub:
                for a, b in pairs:
                    # Avoid leading zeros in numbers of length > 1
                    if cur_len != n or a != "0":
                        result.append(f"{a}{s}{b}")
            return result

        # Call the helper with the full length
        return helper(n)

# Time Complexity (TC):
# - Let n be the input length.
# - Each recursive level generates 5 new combinations (based on `pairs`) for every number in the result of the previous level.
# - The recursion depth is n//2 since two digits are added per level (front and back).
# - At each level:
#   - If there are k numbers from the previous level, this level generates 5 * k numbers.
#   - Total numbers generated = 5^(n//2).
# - Total time complexity: O(5^(n/2)).

# Space Complexity (SC):
# - Recursive stack depth is O(n/2) due to the recursive helper calls.
# - Each level creates a result list that grows exponentially with depth:
#   - At depth d, the result size is 5^d.
# - Total space usage is dominated by the recursion stack: O(n).
# - Final return list: O(5^(n/2)).
# - Combined space complexity: O(5^(n/2)).
