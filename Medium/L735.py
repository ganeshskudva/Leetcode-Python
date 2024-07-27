class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        if not asteroids:
            return st

        for a in asteroids:
            if a > 0:
                st.append(a)
            else:
                while st and 0 < st[-1] < -a:
                    st.pop()
                if not st or st[-1] < 0:
                    st.append(a)
                elif st[-1] == -a:
                    st.pop()

        return st
