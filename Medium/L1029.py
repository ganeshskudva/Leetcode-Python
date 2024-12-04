class Solution:
    def twoCitySchedCost(self, costs):
        # Costs of sending everyone to the first city
        first_city_costs = [cost_a for cost_a, cost_b in costs]
        # Difference in costs for sending to the second city instead
        cost_differences = [cost_b - cost_a for cost_a, cost_b in costs]
        # Minimum cost: Sum of sending everyone to the first city
        # + the cost to switch half of them to the second city
        return sum(first_city_costs) + sum(sorted(cost_differences)[:len(costs) // 2])

# Time Complexity (TC):
# 1. Extracting `first_city_costs` and `cost_differences`:
#    - Requires iterating through the `costs` list once, so this step is O(n).
# 2. Sorting `cost_differences`:
#    - Sorting requires O(n log n), where n is the length of the `costs` list.
# 3. Calculating the sums:
#    - Summing `first_city_costs` and the first n/2 elements of `cost_differences` is O(n).
# Overall, the time complexity is O(n log n), dominated by the sorting step.

# Space Complexity (SC):
# 1. Storage for `first_city_costs` and `cost_differences`:
#    - Both lists require O(n) space.
# 2. Sorting `cost_differences`:
#    - Sorting uses additional O(n) space for the sorted list (depending on the sorting algorithm used).
# Overall, the space complexity is O(n).
