class Twitter:
    def __init__(self):
        # Maps user ID to a list of (timestamp, tweetId)
        self.user_tweets = defaultdict(list)
        # Maps user ID to a set of user IDs they follow
        self.user_following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int):
        # Add tweet to user's tweet list with a timestamp
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        # Get tweets from user and all users they follow
        max_heap = []
        # Add the user's own tweets
        if userId in self.user_tweets:
            for (tweet_time, tweet_id) in self.user_tweets[userId]:
                heapq.heappush(max_heap, (-tweet_time, tweet_id))
        # Add tweets from followed users
        for followeeId in self.user_following[userId]:
            if followeeId in self.user_tweets:
                for (tweet_time, tweet_id) in self.user_tweets[followeeId]:
                    heapq.heappush(max_heap, (-tweet_time, tweet_id))
        # Extract the 10 most recent tweets
        res = []
        while max_heap and len(res) < 10:
            _, tweetId = heapq.heappop(max_heap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int):
        if followerId != followeeId:  # A user cannot follow themselves
            self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        if followeeId in self.user_following[followerId] and followerId != followeeId:
            self.user_following[followerId].remove(followeeId)

# OO Design
class Tweet:
    timestamp = 0

    def __init__(self, id):
        self.id = id
        Tweet.timestamp += 1
        self.time = Tweet.timestamp
        self.nxt = None

class User:
    def __init__(self, id):
        self.id = id
        self.followed = set()
        self.follow(id)
        self.tweet_head = None

    def follow(self, id):
        self.followed.add(id)

    def unfollow(self, id):
        if id in self.followed:
            self.followed.remove(id)

    def post(self, id):
        t = Tweet(id)
        t.nxt = self.tweet_head
        self.tweet_head = t


class Twitter:

    def __init__(self):
        self.user_mp = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_mp:
            self.user_mp[userId] = User(userId)
        self.user_mp[userId].post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res, hp = [], []
        if userId not in self.user_mp:
            return res
        users = self.user_mp[userId].followed
        for u in users:
            twt = self.user_mp[u].tweet_head
            if twt:
                heapq.heappush(hp, (-twt.time, twt))

        n = 0
        while hp and n < 10:
            _, twt = heapq.heappop(hp)
            res.append(twt.id)
            n += 1
            if twt.nxt:
                heapq.heappush(hp, (-twt.nxt.time, twt.nxt))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_mp:
            self.user_mp[followerId] = User(followerId)
        if followeeId not in self.user_mp:
            self.user_mp[followeeId] = User(followeeId)
        self.user_mp[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId not in self.user_mp:
            return
        self.user_mp[followerId].unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
