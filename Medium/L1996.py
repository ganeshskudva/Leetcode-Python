class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # If the properties list is empty, no weak characters can exist
        if not properties:
            return 0

        # Step 1: Sort the characters by their attack values in ascending order.
        # If two characters have the same attack value, sort them by defense in descending order.
        # Sorting by defense in descending order ensures that, for characters with the same attack,
        # a character with a higher defense comes before a character with a lower defense.
        # This prevents counting characters with the same attack as weak against each other.
        properties.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Initialize a variable `mx` to keep track of the maximum defense encountered
        # as we traverse the list from right to left (from the highest attack values to the lowest).
        mx = float('-inf')  # Initially set to negative infinity as we want to compare defense values.

        # Step 3: Initialize `res` to count the number of weak characters.
        res = 0

        # Step 4: Traverse the sorted list from right to left (starting from the last character).
        # This allows us to always check characters with higher attack values first.
        for i in range(len(properties) - 1, -1, -1):
            # Get the defense value of the current character
            defense = properties[i][1]

            # If the current character's defense is less than the maximum defense seen so far,
            # it is considered a "weak" character because there is a stronger character with both
            # higher attack and defense.
            if defense < mx:
                res += 1  # Count this character as weak.

            # Update `mx` to be the maximum defense encountered so far.
            # This ensures that we are always comparing with the strongest defense values.
            mx = max(mx, defense)

        # Step 5: Return the total count of weak characters.
        return res