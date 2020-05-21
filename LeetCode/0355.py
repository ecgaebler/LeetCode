from collections import deque
from heapq import * 
class Twitter:

    def __init__(self):
        self.following = {} # Maps user ID to list of users they follow
        self.next_tweet_id = 0
        self.k = 10 # Included for extensibility if k is not constant 
        self.tweets = {} # Maps user ID to list (deque) of their tweets
        
        

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        # Check if user exists yet. If not, subscribe them to self, then post tweet.
        if user_id not in self.following:
            self.following[user_id] = set([user_id]) # Subscribe user to self
            self.tweets[user_id] = deque()
        self.tweets[user_id].appendleft(self.next_tweet_id)
        self.next_tweet_id += 1
        

    def getNewsFeed(self, user_id: int) -> List[int]:
        if user_id not in self.following:
            return []
        heap = []
        
        # Create a heap with format (-tweet_id, followee_id, tweet_index).
        # Negative tweet_id is used to effectively make the heap a max heap.
        for followee in self.following[user_id]:
            if followee in self.tweets: # Followee has tweets
                latest_tweet = self.tweets[followee][0]
                heappush(heap, (-latest_tweet, followee, 0))
        
        # The heap is essentially a max heap sorted by largest tweet_id. 
        # Pop from heap to determine latest tweet, its tweeter, and the index of that tweet
        # in tweeter's  list of tweets. Add tweet to result deque, increase index, and push
        # (next_largest_tweet, tweeter_id, tweet_index) back onto the heap. 
        result = []
        while len(result) < self.k and heap:
            neg_tweet, user_id, tweet_idx = heappop(heap)
            result.append(-neg_tweet)
            # If there is at least one more tweet left in list, continue adding back onto heap.
            if tweet_idx < len(self.tweets[user_id]) - 1:
                tweet_idx += 1
                heappush(heap, (-tweets[user_id][tweet_idx], user_id, tweet_idx))
        
        return reversed(result)

    def follow(self, follower_id: int, followee_id: int) -> None:
        # If follower or followee doesn't exist yet, make them susbcribe to self.
        if follower_id not in self.following:
            self.following[follower_id] = set([follower_id])
        if followee_id not in self.following:
            self.following[followee_id] = set([followee_id])
        self.following[follower_id].add(followee_id)
        

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.following and follower_id != followee_id:
            self.following[follower_id].discard(followee_id)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)