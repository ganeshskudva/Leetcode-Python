class Twitter:
    def __init__(self):
        """
        Initializes the Twitter object.
        - user_tweets: Maps user ID to a list of tuples (timestamp, tweetId) representing the user's tweets.
        - user_following: Maps user ID to a set of other user IDs they are following.
        - time: A global timestamp counter to assign a unique time to each tweet.
        
        SC: O(U + T), where U is the number of users and T is the total number of tweets posted.
        """
        self.user_tweets = defaultdict(list)  # O(U + T) where U is users and T is tweets.
        self.user_following = defaultdict(set)  # O(U + F), where F is the number of follow relationships.
        self.time = 0  # O(1)

    def postTweet(self, userId: int, tweetId: int):
        """
        Adds a new tweet by the user.
        - Increments the global time for each new tweet.
        - Appends the tweet with its timestamp to the user's tweet list.
        
        TC: O(1), appending to a list is constant time.
        SC: O(1), no additional space except for the tweet being stored.
        """
        self.time += 1  # Increment global timestamp
        self.user_tweets[userId].append((self.time, tweetId))  # Append tweet with timestamp

    def getNewsFeed(self, userId: int):
        """
        Retrieves the 10 most recent tweets in the user's news feed.
        - Includes the user's own tweets and tweets from users they follow.
        - Uses a max heap (negative timestamps) to efficiently fetch the most recent tweets.
        
        TC: O(F * T log(F * T)), where F is the number of followees and T is the number of tweets per user.
        - The log factor comes from maintaining the heap during insertion of tweets.
        - In the worst case, a user might follow F people, and each has T tweets, making the complexity O(F * T).
        SC: O(F * T), where F is the number of followees and T is the number of tweets per user.
        - The heap can hold all the tweets from the user and their followees.
        """
        max_heap = []  # Max-heap to store tweets by timestamp
        # Add the user's own tweets to the heap
        if userId in self.user_tweets:
            for (tweet_time, tweet_id) in self.user_tweets[userId]:
                heapq.heappush(max_heap, (-tweet_time, tweet_id))  # Push negative timestamp for max-heap behavior
        
        # Add tweets from users the current user is following
        for followeeId in self.user_following[userId]:
            if followeeId in self.user_tweets:
                for (tweet_time, tweet_id) in self.user_tweets[followeeId]:
                    heapq.heappush(max_heap, (-tweet_time, tweet_id))  # Push negative timestamp

        # Extract up to 10 most recent tweets
        res = []
        while max_heap and len(res) < 10:
            _, tweetId = heapq.heappop(max_heap)  # Extract the tweetId with the most recent timestamp
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int):
        """
        Allows one user to follow another.
        - Adds the followee to the follower's set of followed users.
        - A user cannot follow themselves.
        
        TC: O(1), adding to a set is constant time.
        SC: O(1), no additional space used except updating the follow set.
        """
        if followerId != followeeId:  # A user cannot follow themselves
            self.user_following[followerId].add(followeeId)  # Add followee to the follower's following list

    def unfollow(self, followerId: int, followeeId: int):
        """
        Allows a user to unfollow another.
        - Removes the followee from the follower's set of followed users.
        - A user cannot unfollow themselves.
        
        TC: O(1), removing from a set is constant time.
        SC: O(1), no additional space used except updating the follow set.
        """
        if followeeId in self.user_following[followerId] and followerId != followeeId:
            self.user_following[followerId].remove(followeeId)  # Remove followee from the follower's following list


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
