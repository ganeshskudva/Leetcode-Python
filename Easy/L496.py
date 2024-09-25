class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp, st = defaultdict(int), []  # mp: map to store next greater element for nums2, st: stack to track decreasing elements
        
        # Traverse nums2 to find the next greater elements
        for n in nums2:
            # While the stack is not empty and the current number is greater than the top of the stack,
            # pop the stack and assign the current number as the next greater element for the popped element
            while st and st[-1] < n:
                mp[st.pop()] = n  # Pop from stack and map it to the current greater element 'n'
            st.append(n)  # Push the current number onto the stack

        # Replace elements in nums1 with their next greater element using the map
        for i in range(len(nums1)):
            # If the current number in nums1 has a next greater element in the map, update it
            # Otherwise, set it to -1 (indicating no greater element was found)
            nums1[i] = mp[nums1[i]] if nums1[i] in mp else -1
        
        return nums1  # Return the updated nums1 list
