class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Inner function to calculate steps between curr and next in the lexicographical tree
        def calSteps(n, n1, n2):
            steps = 0
            # Calculate how many steps between the range [n1, n2) in the lexicographical order
            while n1 <= n:
                # Add the number of valid steps in this range, capped by n + 1
                steps += min(n + 1, n2) - n1
                # Move to the next level in the tree (by multiplying by 10)
                n1 *= 10
                n2 *= 10
            return steps

        curr = 1  # We start from the first number in lexicographical order
        k -= 1  # We decrement k because we're already starting from the first number

        while k > 0:
            steps = calSteps(n, curr, curr + 1)  # Calculate the number of steps to the next sibling
            if steps <= k:
                # If the number of steps is less than or equal to k, we can skip this subtree
                curr += 1  # Move to the next sibling
                k -= steps  # Decrease k by the number of steps we've skipped
            else:
                # If steps are more than k, move to the next level in the current subtree
                curr *= 10  # Go to the next level in the current branch
                k -= 1  # Decrease k by 1 because we moved one step deeper in the tree

        return curr  # Return the k-th lexicographical number
