from typing import List

class Solution:
    def lexicographically_smallest_array(self, arr: List[int], threshold: int) -> List[int]:
        """
        Returns a lexicographically smallest array where values within the
        given threshold are grouped and sorted in place.
        
        Args:
            arr: List[int] - Input array of integers.
            threshold: int - Maximum allowed difference between grouped elements.
        
        Returns:
            List[int] - Modified array.
        """
        # Step 1: Pair each value with its index and sort by values
        # Time Complexity: O(n log n) for sorting
        # Space Complexity: O(n) for storing value-index pairs
        value_index_pairs = sorted((value, idx) for idx, value in enumerate(arr))
        
        # Step 2: Group contiguous values within the threshold
        # Time Complexity: O(n), as we iterate through the sorted list once
        # Space Complexity: O(n), as we store groups
        groups = []
        current_group = [value_index_pairs[0]]  # Start with the first pair

        for i in range(1, len(value_index_pairs)):
            # If the difference is within the threshold, add to the current group
            if value_index_pairs[i][0] - value_index_pairs[i - 1][0] <= threshold:
                current_group.append(value_index_pairs[i])
            else:
                # Otherwise, start a new group
                groups.append(current_group)
                current_group = [value_index_pairs[i]]
        groups.append(current_group)  # Add the last group
        
        # Step 3: Sort indices within each group and update the array
        # Time Complexity: O(n log m) where m is the average group size
        # Space Complexity: O(m) for temporary sorted indices and values
        for group in groups:
            # Extract indices and sort them
            indices = sorted(idx for _, idx in group)
            # Sort the values in the group
            sorted_values = sorted(value for value, _ in group)
            # Assign sorted values back to their original indices
            for idx, value in zip(indices, sorted_values):
                arr[idx] = value

        return arr

# Total Time Complexity:
# 1. Sorting value-index pairs: O(n log n)
# 2. Grouping based on the threshold: O(n)
# 3. Sorting within groups and updating values: O(n log m), where m is the average group size.
# Overall: O(n log n), as the sorting step dominates.

# Total Space Complexity:
# 1. Space for value-index pairs: O(n)
# 2. Space for storing groups: O(n)
# 3. Temporary space for sorting within groups: O(m) at most.
# Overall: O(n), dominated by value-index pairs and groups.
