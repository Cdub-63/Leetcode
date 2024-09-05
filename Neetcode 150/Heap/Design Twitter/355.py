class Twitter:
    def __init__(self):
        """
        Initialize a new Twitter object.
        
        We maintain three data structures:
        
        1. `tweetMap`: a dictionary mapping each user to their tweets.
           Each tweet is stored as a list of two elements: the count (a unique
           identifier), and the tweet id.
        2. `followMap`: a dictionary mapping each user to a set of users they follow.
           The set contains the ids of all users that the key user is following.
        """
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Post a tweet from the given userId.

        This function adds a new tweet to the 'tweetMap' dictionary for the given userId.
        The tweet is represented as a list of two elements: the count (a unique identifier
        for the tweet), and the tweetId.

        We also decrement the 'count' variable to ensure that the next tweet posted will
        have a unique count.
        """
        # Add the new tweet to the 'tweetMap' dictionary. The tweet is represented as a
        # list of two elements: the count (a unique identifier for the tweet), and the
        # tweet id.
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement the 'count' variable to ensure that the next tweet posted will have
        # a unique count.
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Return the 10 most recent tweets from the users that the given userId is following.
        The tweets are ordered from most recent to oldest.

        The algorithm works by using a min-heap to keep track of the most recent tweets
        from all of the users that the given userId is following. The min-heap is ordered
        by the count of each tweet, which is a unique identifier for the tweet that is
        also used to determine the order of the tweets.

        The algorithm works as follows:

        1. Add the given userId to the set of users that the given userId is following.
           This is because we want to include the given userId's own tweets in the
           results.
        2. For each user that the given userId is following, add their most recent tweet
           to the min-heap. The tweet is represented as a list of four elements: the
           count of the tweet, the id of the tweet, the id of the user who posted the
           tweet, and the index of the tweet in the list of tweets for the user.
        3. While the min-heap is not empty and the length of the result list is less than
           10, pop the tweet with the highest count from the min-heap and add it to the
           result list.
        4. Decrement the index of the tweet and add the next tweet from the same user to
           the min-heap if the index is still valid.
        5. Return the result list.
        """
        res = []
        minHeap = []

        # Add the given userId to the set of users that the given userId is following.
        # This is because we want to include the given userId's own tweets in the results.
        self.followMap[userId].add(userId)

        # For each user that the given userId is following, add their most recent tweet
        # to the min-heap. The tweet is represented as a list of four elements: the
        # count of the tweet, the id of the tweet, the id of the user who posted the
        # tweet, and the index of the tweet in the list of tweets for the user.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # While the min-heap is not empty and the length of the result list is less than
        # 10, pop the tweet with the highest count from the min-heap and add it to the
        # result list.
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # Decrement the index of the tweet and add the next tweet from the same user to
            # the min-heap if the index is still valid.
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Makes the user with the given followerId follow the user with the given
        followeeId.

        This method updates the followMap dictionary to reflect the new
        relationship. The followMap dictionary maps each user to a set of all of
        the users that they follow.

        For example, if the user with id 0 follows the user with id 1, then
        followMap[0] will contain the user with id 1.

        Parameters:
            followerId (int): The id of the user who is following
            followeeId (int): The id of the user who is being followed
        """
        # Add the followee to the set of all users that the follower is following
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Makes the user with the given followerId unfollow the user with the given
        followeeId.

        This method updates the followMap dictionary to reflect the new
        relationship. The followMap dictionary maps each user to a set of all of
        the users that they follow.

        For example, if the user with id 0 follows the user with id 1, then
        followMap[0] will contain the user with id 1.

        Parameters:
            followerId (int): The id of the user who is unfollowing
            followeeId (int): The id of the user who is being unfollowed
        """

        # If the followee is indeed in the set of users that the follower is
        # following, then remove them from the set.
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# time complexity: O(n log n)
# space complexity: O(n + m) where n and m are the lengths of list1 and list2