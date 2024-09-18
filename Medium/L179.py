class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # If the input list is empty, return an empty string
        if not nums:
            return ""

        # Convert the integer list to a list of strings
        str_nums = [str(num) for num in nums]

        # Sort the list of strings using a key that compares the concatenation of numbers
        str_nums.sort(key=lambda x: x*10, reverse=True)

        # Edge case: If the largest number after sorting is '0', return '0' (e.g., [0, 0])
        if str_nums[0] == '0':
            return "0"

        # Join all the strings together into the largest number
        return ''.join(str_nums)