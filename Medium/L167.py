class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(tgt):
            lo, hi, mid = 0, len(numbers) - 1, 0

            while lo <= hi:
                mid = (lo + hi) // 2
                if numbers[mid] == tgt:
                    return mid
                if numbers[mid] > tgt:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return -1

        for i in range(len(numbers)):
            idx = bin_search(target - numbers[i])
            if i == idx or idx == -1:
                continue
            return [i + 1, idx + 1] if i < idx else [idx + 1, i + 1]

        return []
