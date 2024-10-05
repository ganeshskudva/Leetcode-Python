## Using Bindary Search
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        This function finds the `k` closest elements to `x` in the sorted array `arr` using binary search.

        Parameters:
        arr (List[int]): A sorted list of integers.
        k (int): The number of closest elements to find.
        x (int): The target value to which the elements should be closest.

        Returns:
        List[int]: A list of `k` elements from `arr` that are closest to `x`, sorted in ascending order.
        """
        # Use binary search to find the starting point of the window.
        left, right = 0, len(arr) - k

        # Perform binary search to find the optimal left boundary.
        while left < right:
            mid = (left + right) // 2

            # Compare the distance between arr[mid] and arr[mid + k] to x
            # If arr[mid] is farther than arr[mid + k], move the left boundary to mid + 1.
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # Return the window of size `k` starting from index `left`.
        return arr[left:left + k]


## Using Sliding Window
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        This function finds the `k` closest elements to the target value `x` in the given sorted array `arr`.
        The result is a subarray of `k` elements, sorted in ascending order, which are the closest to `x`.

        Parameters:
        arr (List[int]): A sorted list of integers.
        k (int): The number of closest elements to find.
        x (int): The target value to which the elements should be closest.

        Returns:
        List[int]: A list of `k` elements from `arr` that are closest to `x`, sorted in ascending order.
        """

        # Initialize two pointers:
        # `left`: This will be the left boundary of our sliding window.
        # `res`: This will store the result, which will hold at most `k` closest elements.
        left, res = 0, []

        # Iterate over the entire array using `right` as the right boundary of the sliding window.
        for right in range(len(arr)):
            # Append the current element to the result list `res`.
            res.append(arr[right])

            # Calculate the current window size.
            win_sz = right - left + 1

            # If the window size exceeds `k`, we need to shrink the window from either the left or the right.
            if win_sz > k:
                # Compare the distance of the leftmost element (`arr[left]`) and the rightmost element (`arr[right]`) from `x`.
                # Remove the element that is farther away from `x` to maintain the closest `k` elements.
                if abs(arr[left] - x) > abs(arr[right] - x):
                    # If the leftmost element is farther from `x`, remove it from the result.
                    res.pop(0)
                else:
                    # Otherwise, if the rightmost element is farther from `x`, remove it from the result.
                    res.pop()
                
                # After shrinking the window, move the `left` pointer to the right.
                left += 1
        
        # The result list `res` will contain `k` elements that are closest to `x`. Since the input `arr` is already sorted,
        # the result will also be sorted in ascending order.
        return res
