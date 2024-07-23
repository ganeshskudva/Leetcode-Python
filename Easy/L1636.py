class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each element
        count = Counter(nums)
        
        # Sort by frequency, and then by value (in descending order for ties)
        nums.sort(key=lambda x: (count[x], -x))
        
        return nums
