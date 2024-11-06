class SparseVector:
    def __init__(self, nums: List[int]):
        # Dictionary to store only the non-zero elements with their indices
        self.seen = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.seen[i] = n  # Store index and value for non-zero elements

        # TC: O(n), where n is the length of nums, since we iterate over all elements in nums.
        # SC: O(k), where k is the number of non-zero elements in nums, as we store only non-zero elements in the dictionary.

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        # Iterate only over non-zero elements in vec.seen to calculate the dot product
        for j, n in vec.seen.items():
            if j in self.seen:
                res += n * self.seen[j]

        # TC: O(min(k1, k2)), where k1 and k2 are the numbers of non-zero elements in self and vec, respectively.
        # We only iterate over the non-zero elements in vec.seen and check for their presence in self.seen.
        # SC: O(1), as we only use a constant amount of extra space for the result.

        return res

		
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
