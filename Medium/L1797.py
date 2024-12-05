class AuthenticationManager:

    def __init__(self, timeToLive: int):
        # Initialize the token store (dictionary) and time-to-live value
        self.mp = defaultdict(int)  # SC: O(n), where n is the number of tokens stored
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        # Generate a new token with its expiration time
        self.mp[tokenId] = currentTime + self.ttl
        # TC: O(1)

    def renew(self, tokenId: str, currentTime: int) -> None:
        # Renew a token's expiration time if it exists and is not expired
        if tokenId not in self.mp:
            return  # Token does not exist, do nothing
        if self.mp[tokenId] > currentTime:
            # Update token expiration time
            self.mp[tokenId] = currentTime + self.ttl
        # TC: O(1)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # Count tokens that have not expired
        cnt = 0
        for v in self.mp.values():
            if v > currentTime:
                cnt += 1
        return cnt
        # TC: O(n), where n is the number of tokens stored
        # SC: O(1) additional space for the counter
