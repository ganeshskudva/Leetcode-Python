class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize the result array 'ret' with [-1, -1], which represents that
        # the target value is not found. This will be returned if the target is not found.
        ret = [-1, -1]
        
        # If the input list 'nums' is empty, there's nothing to search.
        # Return [-1, -1] immediately as the target cannot be found in an empty list.
        if not nums:
            return ret

        # Helper function that performs a binary search to find either the first or last occurrence of the target.
        # 'start' indicates the index to begin searching from (typically 0).
        # 'first' is a boolean flag: if True, the function searches for the first occurrence;
        # if False, it searches for the last occurrence of the target.
        def bs(start, first):
            # Initialize binary search bounds:
            # 'lo' is the lower bound, starting from the provided 'start' index.
            # 'hi' is the upper bound, starting from the last index of the array.
            # 'res' is initialized to -1, and it will store the index of the target if found.
            lo, hi, res = start, len(nums) - 1, -1

            # Perform binary search while 'lo' is less than or equal to 'hi'.
            while lo <= hi:
                # Calculate the middle index 'mid' in the current search range.
                # This avoids potential overflow in other languages (not an issue in Python).
                mid = lo + (hi - lo) // 2
                
                # If the value at 'mid' is less than the target, search in the right half.
                if nums[mid] < target:
                    lo = mid + 1  # Move 'lo' to 'mid + 1' to search the right half.
                
                # If the value at 'mid' is greater than the target, search in the left half.
                elif nums[mid] > target:
                    hi = mid - 1  # Move 'hi' to 'mid - 1' to search the left half.
                
                # If 'nums[mid]' equals the target:
                else:
                    # Update 'res' to store the index where the target is found.
                    res = mid
                    
                    # If we are looking for the first occurrence of the target:
                    if first:
                        # Move 'hi' to 'mid - 1' to continue searching in the left half.
                        # This ensures we find the first occurrence, even if there are duplicates.
                        hi = mid - 1
                    # If we are looking for the last occurrence of the target:
                    else:
                        # Move 'lo' to 'mid + 1' to continue searching in the right half.
                        # This ensures we find the last occurrence, even if there are duplicates.
                        lo = mid + 1

            # Return the final index of the target ('res') if found, or -1 if not found.
            return res

        # First, search for the first occurrence of the target by calling 'bs' with 'first=True'.
        ret[0] = bs(0, True)
        
        # If the target is not found (i.e., ret[0] is still -1), return [-1, -1] immediately.
        if ret[0] == -1:
            return ret

        # If the first occurrence is found, search for the last occurrence of the target
        # by calling 'bs' with 'first=False'. This will find the last occurrence.
        ret[1] = bs(0, False)

        # Return the result array 'ret', which contains the first and last occurrence
        # of the target. If the target is not found, ret will remain [-1, -1].
        return ret
