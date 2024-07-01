class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def is_odd(n):
            return n % 2 > 0

        for i in range(len(arr) - 2):
            if is_odd(arr[i]):
                if is_odd(arr[i + 1]) and is_odd(arr[i + 2]):
                    return True

        return False
