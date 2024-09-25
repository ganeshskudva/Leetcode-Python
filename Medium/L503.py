class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nxt = [-1] * len(nums)  # Initialize result list 'nxt' with -1, assuming no greater element found
        st = []  # Stack to store indices of elements for which we haven't found the next greater element yet
        n = len(nums)  # Length of the input list 'nums'

        # Iterate over the list twice to simulate a circular array
        for i in range(n * 2):  # Loop twice over the array
            num = nums[i % n]  # Use modulo to wrap around the index for the circular effect
            
            # While stack is not empty and the current number is greater than the element at the top index in the stack
            while st and nums[st[-1]] < num:
                nxt[st.pop()] = num  # Pop from the stack and set the current number as the next greater element
            
            # In the first pass (i < n), push the index onto the stack
            if i < n:
                st.append(i)

        return nxt  # Return the list with next greater elements
