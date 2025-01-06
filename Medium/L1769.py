class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)  # Result array to store the minimum operations for each box
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)

        # Calculate costs from left to right
        for i in range(1, n):
            if boxes[i - 1] == '1': 
                leftCount += 1  # Count of '1's to the left of the current box
            leftCost += leftCount  # Increment left cost by the total number of left '1's
            ans[i] = leftCost  # Store the cost for the current box

        # Calculate costs from right to left
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1': 
                rightCount += 1  # Count of '1's to the right of the current box
            rightCost += rightCount  # Increment right cost by the total number of right '1's
            ans[i] += rightCost  # Add the cost from the right to the existing left cost

        return ans

# Time Complexity (TC): O(n) - Two passes over the string of length n.
# Space Complexity (SC): O(n) - Result array `ans` of size n.
