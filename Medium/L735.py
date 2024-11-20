# without stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        idx = 0  # Acts like the stack pointer
        
        for a in asteroids:
            while idx > 0 and asteroids[idx - 1] > 0 and asteroids[idx - 1] < -a:
                idx -= 1  # Simulate popping the stack
            if idx == 0 or asteroids[idx - 1] < 0 or a > 0:
                asteroids[idx] = a  # Simulate pushing onto the stack
                idx += 1
            elif asteroids[idx - 1] == -a:
                idx -= 1  # Destroy both asteroids (simulate pop)

        return asteroids[:idx]  # Return the surviving asteroids

# Time Complexity (TC): O(n)
# - Each asteroid is processed once, with each push or pop taking O(1).
# Total: O(n).

# Space Complexity (SC): O(1)
# - No additional data structures are used, and the input list is modified in place.


# with stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []  # Stack to store surviving asteroids
        if not asteroids:
            return st  # If input is empty, return an empty list

        for a in asteroids:
            if a > 0:  # Positive asteroids move to the right
                st.append(a)
            else:  # Negative asteroid moving to the left
                while st and 0 < st[-1] < -a:  # Positive asteroid smaller than current negative
                    st.pop()  # Destroy the smaller positive asteroid
                if not st or st[-1] < 0:  # No collision or only negative asteroids left
                    st.append(a)  # Add the negative asteroid
                elif st[-1] == -a:  # Equal size, destroy both
                    st.pop()

        return st  # Return surviving asteroids

# Time Complexity (TC): O(n)
# - Each asteroid is pushed or popped from the stack at most once.
# - Traversing the `asteroids` list takes O(n).
# Total: O(n).

# Space Complexity (SC): O(n)
# - The stack `st` can store all asteroids in the worst case (e.g., no collisions).
# Total: O(n).
