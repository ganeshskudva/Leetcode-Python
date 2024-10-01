class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Initialize a frequency array to keep track of the remainders when
        # elements of 'arr' are divided by 'k'. The size of this array is 'k',
        # and each index represents a remainder from 0 to k-1.
        freq = [0] * k
        
        # Iterate through each number in the array.
        for n in arr:
            # Compute the remainder when 'n' is divided by 'k'. This will tell us
            # how much is left after dividing by 'k'.
            n %= k
            
            # If 'n' is negative, add 'k' to make it positive. This ensures that all
            # remainders are in the range [0, k-1]. For example, a remainder of -1
            # should be treated as 'k-1'.
            if n < 0:
                n += k
                
            # Increment the count of the remainder in the frequency array.
            freq[n] += 1

        # Special case: If there are any numbers whose remainder is exactly 0,
        # there must be an even number of such numbers, because pairs of numbers
        # that sum to 0 mod 'k' will both have a remainder of 0. Thus, if the count
        # of such numbers is odd, return False.
        if freq[0] % 2 != 0:
            return False

        # Check if every remainder 'i' can be paired with 'k - i' to form a sum
        # divisible by 'k'. For instance, if 'k = 5', then remainder '1' must pair
        # with remainder '4' because 1 + 4 = 5, which is divisible by 'k'.
        for i in range(1, (k // 2) + 1):
            # The frequency of remainder 'i' must match the frequency of 'k - i',
            # because these remainders must pair with each other. If they don't match,
            # return False because it won't be possible to pair all numbers.
            if freq[i] != freq[k - i]:
                return False

        # If all conditions are satisfied, return True. This means the array
        # can be rearranged such that every pair of numbers sums to a multiple of 'k'.
        return True
