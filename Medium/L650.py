class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}

        def compute_steps(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 0  # No steps needed for 1 'A'
            
            result = n  # The worst case, we have to do 'Paste' n-1 times
            for i in range(n - 1, 1, -1):
                if n % i == 0:
                    result = compute_steps(i) + (n // i)
                    break
            
            memo[n] = result
            return result

        return compute_steps(n)
