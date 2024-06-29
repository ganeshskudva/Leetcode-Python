class Solution:

    def __init__(self, w: List[int]):
        self.w_sums = [0] * len(w)
        self.w_sums[0] = w[0]
        for i in range(1, len(w)):
            self.w_sums[i] = self.w_sums[i - 1] + w[i]

    def pickIndex(self) -> int:
        n, rand_idx = len(self.w_sums), random.randint(1, self.w_sums[-1])
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2
            if self.w_sums[mid] == rand_idx:
                return mid
            elif self.w_sums[mid] < rand_idx:
                left = mid + 1
            else:
                right = mid

        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
