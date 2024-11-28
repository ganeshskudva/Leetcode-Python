class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res, st, mod, n = 0, [-1], 1000000007, len(arr)

        # Iterate through the array and one extra iteration for handling end conditions
        for i in range(n + 1):
            curr_val = arr[i] if i < n else 0  # Use 0 as a sentinel to process remaining stack elements

            # Maintain a monotonic stack for tracking indices of increasing elements
            while st[len(st) - 1] != -1 and curr_val < arr[st[len(st) - 1]]:
                index = st.pop()  # Index of the element being processed
                new_top = st[len(st) - 1]  # Index of the next element in the stack
                
                # Calculate the contribution of arr[index] as the minimum of all subarrays that include it
                left, right = index - new_top, i - index  # Distance to the left and right boundaries
                add = (left * right * arr[index]) % mod  # Add contribution modulo `mod`
                res += add
                res %= mod  # Ensure result stays within modulo range

            st.append(i)  # Push the current index onto the stack

        return res

# Time Complexity (TC):
# - The loop runs `n+1` times.
# - Each element is pushed onto the stack once and popped once, resulting in an amortized O(n) complexity for stack operations.
# - Overall TC: O(n).

# Space Complexity (SC):
# - The stack can hold at most `n+1` indices.
# - Additional variables (res, mod, etc.) use O(1) space.
# - Overall SC: O(n) for the stack.
