class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Memoization map to store if we can jump from a specific index
        mp = defaultdict(bool)

        # Helper function with memoization to check if we can reach the end starting from 'idx'
        def solve(idx=0):
            # Base case: If the index is at or beyond the last index, return True
            if idx >= len(nums) - 1:
                return True
            
            # If the current index has a value of 0, we can't move further from here
            if nums[idx] == 0:
                mp[idx] = False
                return mp[idx]

            # If we've already computed the result for this index, return it
            if idx in mp:
                return mp[idx]

            # Calculate the maximum jump we can make from this index
            max_jump = min(len(nums) - 1, idx + nums[idx])
            
            # Try all possible jumps from the current index
            for i in range(idx + 1, max_jump + 1):
                # If jumping to index 'i' is successful, mark the current index as reachable
                if i not in mp and solve(i):
                    mp[idx] = True
                    return mp[idx]

            # If none of the jumps work, mark the current index as not reachable
            mp[idx] = False
            return mp[idx]

        # Start solving from index 0
        return solve()
