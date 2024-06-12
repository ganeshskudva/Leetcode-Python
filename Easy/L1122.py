class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
      ans, cnt = [], collections.Counter(arr1)         # Count each number in arr1
      for i in arr2:                                   # Sort the common numbers in both arrays by the order of arr2.
          for _ in range(cnt.pop(i)):
              ans.append(i)
      for i in range(min(arr1), max(arr1) + 1):        # Sort the numbers only in arr1.
          for _ in range(cnt.pop(i, 0)):
              ans.append(i)
      return ans
