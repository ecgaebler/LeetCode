import java.util.*;
class Twitter {
    Deque<Pair<Integer, Integer>> tweets;
    HashMap<Integer, Integer> tweetOwner;
    HashMap<Integer, HashSet<Integer>> followedBy; //maps user ID to set of users they follow
    HashMap<Integer, HashSet<Integer>> followersOf; //maps user ID to set of users following them
    

    /** Initialize your data structure here. */
    public Twitter() {
        tweets = new LinkedList<>();
        tweetOwner = new HashMap<>();
        followedBy = new HashMap<>();
        followersOf = new HashMap<>();
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        tweets.addFirst(new Pair<Integer, Integer>(tweetId, userId));
        tweetOwner.put(tweetId, userId);
        follow(userId, userId);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
        if(!followedBy.containsKey(userId)) {
            return Collections.emptyList();
        }
        List<Integer> displayTweets = new LinkedList<>();
        for(Pair<Integer, Integer>tweet: tweets) {
            if(followedBy.get(userId).contains(tweet.getValue())) {
                displayTweets.add(tweet.getKey());
            }
            if(displayTweets.size() == 10) {
                break;
            }
        }
        return displayTweets;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if(!followedBy.containsKey(followeeId)) {
            followedBy.put(followeeId, new HashSet<Integer>());
            followersOf.put(followeeId, new HashSet<Integer>());
            follow(followeeId, followeeId);
        }
        if(!followedBy.containsKey(followerId)) {
            followedBy.put(followerId, new HashSet<Integer>());
            followersOf.put(followerId, new HashSet<Integer>());
            follow(followerId, followerId);
        }
        followedBy.get(followerId).add(followeeId);
        followersOf.get(followeeId).add(followerId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if(followerId == followeeId || 
           !followedBy.containsKey(followerId) || 
           !followedBy.get(followerId).contains(followeeId)) {
            return;
        }
        followedBy.get(followerId).remove(followeeId);
        followersOf.get(followeeId).remove(followerId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */