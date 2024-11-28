class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # To store all combinations

        # Helper function to perform backtracking
        def solve(current_combination, start, k):
            if k == 0:  # Base case: if no more elements are needed
                res.append(current_combination[:])  # Add a copy of the current combination
                return

            # Iterate through numbers from `start` to `n`
            for i in range(start, n + 1):
                current_combination.append(i)  # Include the current number
                solve(current_combination, i + 1, k - 1)  # Recurse with updated parameters
                current_combination.pop()  # Backtrack by removing the last element

        solve([], 1, k)  # Start with an empty combination and the first number
        return res

# Time Complexity (TC):
# - The number of combinations is \( \binom{n}{k} \), which is the result size.
# - For each valid combination, the algorithm performs \( O(k) \) work to build the combination.
# - Therefore, the overall complexity is \( O(k \times \binom{n}{k}) \).

# Space Complexity (SC):
# - The recursion depth is \( O(k) \) due to the call stack.
# - Each recursive call uses \( O(k) \) for the temporary combination list.
# - Overall space complexity: \( O(k) \).
