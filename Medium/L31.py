class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next lexicographical permutation of the numbers.
        If such arrangement is not possible, it rearranges it to the lowest possible order.
        """

        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If such element is found, find the next larger element to swap with
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap elements at i and j
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the elements after index i to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:])