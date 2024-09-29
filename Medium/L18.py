class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the input array to facilitate the two-pointer approach and handle duplicates
        nums.sort()

        # Recursive function to solve the k-sum problem (initially set for k = 4 for fourSum)
        def solve(start=0, k=4, tgt=target):
            # n is the length of nums, res is the list to store the result sets
            n, res = len(nums), []
            
            # Base case: if k == 2, solve the 2-sum problem using the two-pointer approach
            if k == 2:
                # Initialize two pointers: left starts at `start`, right starts at the end of the array
                left, right = start, n - 1
                while left < right:
                    tot = nums[left] + nums[right]  # Calculate the sum of nums[left] and nums[right]
                    
                    if tot == tgt:  # If the sum matches the target, add the pair to the result
                        res.append([nums[left], nums[right]])
                        
                        # Skip duplicates on the left side
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        # Skip duplicates on the right side
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers inward after finding a valid pair
                        left, right = left + 1, right - 1
                    
                    elif tot < tgt:  # If the sum is less than the target, move the left pointer to the right to increase the sum
                        left += 1
                    
                    else:  # If the sum is greater than the target, move the right pointer to the left to decrease the sum
                        right -= 1
            
            # Recursive case: if k > 2, reduce the problem to (k-1)-sum by fixing one number and solving (k-1)-sum
            else:
                # Iterate over the array, starting from `start`, and fix the current number for each recursive call
                for i in range(start, n - (k - 1)):  # Ensure there are enough elements left for k numbers
                    
                    # Skip duplicates to avoid generating repeated sets
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    
                    # Early pruning to avoid unnecessary recursive calls:
                    # If the smallest possible sum (nums[i] * k) is larger than target, skip.
                    # If the largest possible sum (nums[i] + (k-1) * nums[-1]) is smaller than target, skip.
                    if nums[i] * k > tgt or nums[i] + nums[-1] * (k - 1) < tgt:
                        continue
                    
                    # Recursively solve the (k-1)-sum problem for the remaining part of the array
                    tmp = solve(i + 1, k - 1, tgt - nums[i])
                    
                    # Add the current number to the result sets from the recursive call
                    for t in tmp:
                        res.append([nums[i]] + t)
            
            # Return the result set for this particular recursive call
            return res

        # Start solving the 4-sum problem by calling the `solve` function with k = 4
        return solve()
