class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # If the number is 1, it's not a perfect number (by definition, perfect numbers are > 1)
        if num == 1:
            return False
        
        # Initialize the sum of divisors to 1 (since 1 is always a divisor)
        res = 1
        
        # Iterate over possible divisors from 2 to the square root of the number
        # We check up to sqrt(num) because divisors come in pairs (i, num//i)
        for i in range(2, int(num**0.5) + 1):
            # If 'i' is a divisor of 'num'
            if num % i == 0:
                # Add both divisors (i and num//i) to the sum
                res += i + num // i
        
        # Check if the sum of divisors equals the number itself
        return res == num

# Time Complexity (TC):
# The time complexity is O(sqrt(n)), where `n` is the input number `num`.
# We only iterate from 2 up to the square root of `num` to find divisors because divisors come in pairs (i, num//i).
# Thus, the loop runs approximately sqrt(n) times, making the time complexity O(sqrt(n)).

# Space Complexity (SC):
# The space complexity is O(1) since we are using only a constant amount of extra space (variables `res` and `i`).
# No additional space is used that grows with the input size, so the space complexity is constant.
