# recursive
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term in the 'Count and Say' sequence.

        Args:
        n (int): The position of the sequence to generate.

        Returns:
        str: The nth term in the sequence.

        Time Complexity: O(2^n), where n is the input number.
            - Each term is built by iterating through the previous term, 
              which roughly doubles in size for each step.

        Space Complexity: O(2^n), as each recursive call holds the result of the previous term, 
        which grows exponentially in size.
        """
        if n == 1:  # Base case: the first term is always '1'
            return '1'
    
        # Recursively generate the previous term in the sequence
        prev = self.countAndSay(n - 1)
        curr, cnt = [], 1  # Initialize the current term and count
        
        # Iterate through the previous term to build the current term
        for i in range(1, len(prev)):
            if prev[i - 1] == prev[i]:  # If the current character matches the previous one
                cnt += 1
            else:
                # Append the count and the character to the current term
                curr.append(str(cnt))
                curr.append(prev[i - 1])
                cnt = 1  # Reset the count for the new character

        # Append the last group
        curr.append(str(cnt))
        curr.append(prev[-1])
    
        return ''.join(curr)  # Combine the list into a string

# Time Complexity: O(2^n), where n is the input number.
# Space Complexity: O(2^n), due to recursive calls and the exponential growth of the sequence.

# iterative
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term in the 'Count and Say' sequence using an iterative approach.

        Args:
        n (int): The position of the sequence to generate.

        Returns:
        str: The nth term in the sequence.

        Time Complexity: O(2^n), where n is the input number.
            - The sequence length roughly doubles at each step.
        Space Complexity: O(2^n), as the space required for the sequence grows exponentially.
        """
        # Start with the base case
        result = "1"

        for _ in range(1, n):  # Iterate from 2 to n
            curr, count = [], 1  # Initialize current sequence and count
            
            # Process the current result to build the next term
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:  # If current and previous characters are the same
                    count += 1
                else:
                    # Append count and character to the current sequence
                    curr.append(str(count))
                    curr.append(result[i - 1])
                    count = 1  # Reset count for the new character
            
            # Append the last group
            curr.append(str(count))
            curr.append(result[-1])
            
            # Update result to the newly generated sequence
            result = ''.join(curr)

        return result

# Time Complexity: O(2^n), where n is the input number.
# Space Complexity: O(2^n), for the exponential growth of the sequence.
