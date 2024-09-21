class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Result list to store lexicographical numbers
        res = []

        # Recursive function to generate numbers in lexicographical order
        def solve(curr):
            # Add the current number to the result list
            res.append(curr)

            # Try to generate numbers by appending digits 0 to 9
            for i in range(10):
                next_num = 10 * curr + i
                # If the next number exceeds n, stop further recursion
                if next_num > n:
                    return
                # Recursively generate the next lexicographical number
                solve(next_num)

        # Start the recursion from numbers 1 to 9
        for i in range(1, 10):
            if i > n:  # Early exit if `i` exceeds `n` (redundant for large values of `n`)
                break
            solve(i)

        # Return the lexicographically ordered result
        return res