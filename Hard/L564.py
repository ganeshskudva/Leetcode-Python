class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        i = (length // 2 - 1) if length % 2 == 0 else (length // 2)
        left = int(n[:i + 1])

        # Closure to generate the palindrome
        def generate_palindrome(left_half: int, is_even: bool) -> int:
            result = left_half
            if not is_even:
                left_half //= 10
            while left_half > 0:
                result = result * 10 + left_half % 10
                left_half //= 10
            return result

        # Generate possible candidates using closure
        candidates = []
        candidates.append(generate_palindrome(left, length % 2 == 0))  # +0
        candidates.append(generate_palindrome(left + 1, length % 2 == 0))  # +1
        candidates.append(generate_palindrome(left - 1, length % 2 == 0))  # -1
        candidates.append(10**(length - 1) - 1)  # 999...9
        candidates.append(10**length + 1)  # 100...001

        # Find the nearest palindrome
        original_num = int(n)
        closest_palindrome = None
        smallest_diff = float('inf')

        for candidate in candidates:
            if candidate == original_num:
                continue
            diff = abs(candidate - original_num)
            if diff < smallest_diff or (diff == smallest_diff and candidate < closest_palindrome):
                closest_palindrome = candidate
                smallest_diff = diff

        return str(closest_palindrome)
