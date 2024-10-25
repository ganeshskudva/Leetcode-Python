class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        # If there are no digits, return an empty list
        if not digits:
            return ans

        # Map of digits to corresponding letters
        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # Helper function to generate combinations recursively
        def solve(idx, tmp=[]):
            # Base case: If idx exceeds the length of digits, return (shouldn't happen)
            if idx > len(digits):
                return

            # When the current combination has reached the length of digits
            if len(tmp) == len(digits):
                ans.append(''.join(tmp))  # O(L) where L is the length of digits
                return

            # Get the current digit
            curr_dig = digits[idx]
            # Loop through all the possible letters for this digit
            for letter in mp[curr_dig]:
                tmp.append(letter)  # Add the letter to the temporary combination
                solve(idx + 1, tmp)  # Recursively call for the next digit
                del tmp[-1]  # Backtrack by removing the last added letter

        # Start the recursive process
        solve(0)
        return ans

# Time Complexity (TC):
# - For each digit, there are up to 4 possible letters (e.g., "7" and "9" have 4 letters).
# - The total number of possible combinations is 3^n * 4^m, where n is the number of digits that map to 3 letters (like "2", "3", etc.), and m is the number of digits that map to 4 letters (like "7", "9").
# - For each combination generated, it takes O(L) time to join the letters into a string (where L is the length of the digits).
# - Therefore, the total time complexity is O(3^n * 4^m * L), where n is the number of digits with 3 letters, m is the number of digits with 4 letters, and L is the length of the input digits.

# Space Complexity (SC):
# - The recursion depth can go as deep as the number of digits, so the recursive call stack can take O(L) space, where L is the number of digits.
# - Temporary storage for the combinations (in `tmp`) takes O(L) space.
# - The result list `ans` will store up to 3^n * 4^m combinations.
# - Overall space complexity is O(L + 3^n * 4^m), where L is the length of the digits and 3^n * 4^m is the number of possible combinations.

