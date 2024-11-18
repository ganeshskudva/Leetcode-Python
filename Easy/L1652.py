class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # `n` is the length of the original code list
        # `code` is transformed into a prefix sum array of the concatenated array (code + code)
        n, code = len(code), list(accumulate(code + code))
        
        # If k < 0, we need to sum elements to the left (backwards), so adjust the indices accordingly
        if k < 0:
            return [code[i] - code[i + k] for i in range(n - 1, 2 * n - 1)]
        
        # If k > 0, we need to sum elements to the right, so calculate the difference of the prefix sums
        if k > 0:
            return [code[i + k] - code[i] for i in range(n)]
        
        # If k == 0, all elements in the output should be 0
        return [0] * n

# Time Complexity (TC):
# - Building the prefix sum array `accumulate(code + code)` takes O(2n) = O(n), where `n` is the length of the input list.
# - The list comprehension iterates `n` times to compute the result, and each operation inside takes O(1).
# - Overall TC: O(n).

# Space Complexity (SC):
# - The prefix sum array `code` is constructed with a length of `2n`, requiring O(2n) = O(n) additional space.
# - The output list requires O(n) space.
# - Overall SC: O(n).
