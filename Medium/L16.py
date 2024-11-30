class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        # Sort the array to use a two-pointer technique
        num.sort()

        # Initialize result to the sum of the first three elements
        result = num[0] + num[1] + num[2]

        # Iterate through each element as the first number in the triplet
        for i in range(len(num) - 2):
            # Use two pointers to find the closest sum to the target with `num[i]`
            j, k = i + 1, len(num) - 1
            while j < k:
                # Calculate the current sum of the triplet
                total = num[i] + num[j] + num[k]

                # If the current sum is exactly the target, we found the closest possible
                if total == target:
                    return total

                # If the current sum is closer to the target than the previous result, update result
                if abs(total - target) < abs(result - target):
                    result = total

                # Move the pointers based on whether the current sum is less or more than the target
                if total < target:
                    j += 1  # Increase the sum by moving the left pointer to the right
                elif total > target:
                    k -= 1  # Decrease the sum by moving the right pointer to the left

        # Return the closest sum found
        return result

# Time Complexity (TC): O(n^2)
# - Sorting the array takes O(n log n).
# - The two-pointer approach within the loop iterates in O(n^2), as for each element `i`, we process
#   the subarray with two pointers, leading to a quadratic time complexity.

# Space Complexity (SC): O(1)
# - Aside from the input array and a few variables for pointers and calculations, 
#   no extra space is used, resulting in O(1) additional space complexity.
