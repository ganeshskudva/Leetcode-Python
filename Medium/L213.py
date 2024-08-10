class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def get_max(i, rob_first):
            # Base case: when index exceeds the array bounds or last house should not be robbed
            if i >= len(nums) or (i == len(nums) - 1 and rob_first):
                return 0

            # Check if the result is already computed and stored in dp
            if (i, rob_first) in dp:
                return dp[(i, rob_first)]

            # If it's the first house, we mark rob_first as True
            if i == 0:
                rob = get_max(i + 2, True) + nums[i]
            else:
                rob = get_max(i + 2, rob_first) + nums[i]
            
            # Option to skip the current house
            not_rob = get_max(i + 1, rob_first)

            # Store the result in dp and return the maximum of robbing or not robbing the house
            dp[(i, rob_first)] = max(rob, not_rob)
            return dp[(i, rob_first)]

        # Start the recursive function from index 0 and without robbing the first house
        return get_max(0, False)
