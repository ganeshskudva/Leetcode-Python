class ProductOfNumbers:
    def __init__(self):
        # Initialize the list to store cumulative products and reset the product.
        self.data = []
        self.product = 1

    def add(self, num: int) -> None:
        # If the number is not zero, multiply the current product and append to the data list.
        if num != 0:
            self.product *= num
            self.data.append(self.product)
        else:
            # If a zero is added, reset the product and clear the data list.
            self.data = []
            self.product = 1

    def getProduct(self, k: int) -> int:
        # If there are fewer than k elements, a zero was added, so return 0.
        if len(self.data) < k:
            return 0
        # Return the product of the last k elements using integer division.
        return self.data[-1] if len(self.data) == k else self.data[-1] // self.data[-1 - k]

# Time Complexity (TC):
# 1. The `add()` method:
#    - Appending to the list (`self.data.append(...)`) takes O(1) time.
#    - Multiplying the product by `num` is also O(1).
#    - In case of zero, resetting the list and the product takes O(1).
#    Therefore, the time complexity of `add()` is O(1).
#
# 2. The `getProduct()` method:
#    - Accessing the last `k` elements of the list and performing integer division takes O(1) time.
#    Therefore, the time complexity of `getProduct()` is O(1).
#
# Overall, both `add()` and `getProduct()` run in O(1) time.

# Space Complexity (SC):
# - The space complexity is determined by the size of the `data` list, which stores cumulative products.
# - In the worst case, `self.data` will store O(n) elements, where `n` is the total number of elements added.
# Therefore, the overall space complexity is O(n), where `n` is the number of elements added to the structure.
