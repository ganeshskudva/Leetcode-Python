class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Array to simulate population changes (years range from 1950 to 2050)
        population = [0] * 101  # 101 because 2050 - 1950 + 1 = 101 years

        # Update population changes for each birth and death
        for birth, death in logs:
            population[birth - 1950] += 1  # Increment population for birth year
            population[death - 1950] -= 1  # Decrement population for death year

        # Calculate the prefix sum to get the population for each year
        max_population, max_year, current_population = 0, 1950, 0
        for year in range(101):
            current_population += population[year]
            if current_population > max_population:
                max_population = current_population
                max_year = 1950 + year  # Convert index back to the actual year

        return max_year

# Time Complexity (TC):
# 1. Iterating over logs to update the `population` array: O(n), where n is the number of logs.
# 2. Iterating over the 101 years to calculate the prefix sum and determine the maximum population: O(101) ≈ O(1) (constant).
# Overall TC: O(n).

# Space Complexity (SC):
# 1. The `population` array requires O(101) ≈ O(1) (constant) space.
# Overall SC: O(1).
