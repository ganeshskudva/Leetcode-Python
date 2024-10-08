class Solution:
    def minSwaps(self, s: str) -> int:
        # Initialize two variables:
        # 'balance' keeps track of how many unmatched opening brackets we have.
        # 'swap' counts the minimum number of swaps required to make the string balanced.
        balance, swap = 0, 0
        
        # Iterate over each character in the string 's'.
        # TC: O(n), where n is the length of the string 's', as we process each character exactly once.
        for char in s:
            # If we encounter an opening bracket '[', increment the balance.
            # This means we have one more opening bracket to match with a closing bracket.
            if char == '[':
                balance += 1
                
            # If we encounter a closing bracket ']', decrement the balance.
            # This indicates that we are trying to match it with a previous opening bracket.
            else:
                balance -= 1
            
            # If balance goes negative, it means there are more closing brackets than opening ones.
            # In a valid bracket sequence, this cannot happen.
            # Hence, we need a swap to fix this imbalance.
            if balance == -1:
                # Increment the swap counter since we need to fix this imbalance.
                swap += 1
                
                # Reset the balance to 1, because we've "virtually" swapped a closing bracket with
                # an opening bracket, thus creating an opening bracket at this point.
                balance = 1
        
        # Return the total number of swaps needed to make the string balanced.
        # TC: O(1), since returning a variable is constant time.
        return swap

# SC: O(1), as we only use constant space for the 'balance' and 'swap' variables, regardless of the input size.
