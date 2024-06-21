class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisfied, unsatisfied, trickSatisfied = 0, 0, 0

        for end, customer in enumerate(customers):
            # Expand ---> Categorize satisfied/unsatisfied based on regular grumpy status
            if not grumpy[end]:
                satisfied += customer
            else:
                unsatisfied += customer

            if end >= X:  # Window size is > X, Shrink --->
                unsatisfied -= customers[end - X] * grumpy[
                    end - X]  # To maintain size of window X, remove unsatisfied customer from left end of the window

            trickSatisfied = max(trickSatisfied, unsatisfied)

        return satisfied + trickSatisfied
