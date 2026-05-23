class Twitter:

    def __init__(self):
        self.followlist = defaultdict(set)
        self.postlist = defaultdict(deque)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postlist[userId].append((self.timestamp, tweetId))
        self.timestamp += 1
        if len(self.postlist[userId]) > 10:
            self.postlist[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        sources = [userId] + list(self.followlist[userId])
        min_heap = []
        for uid in sources:
            for time, tid in self.postlist[uid]:
                heapq.heappush(min_heap, (time, tid))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            time, tid = heapq.heappop(min_heap)
            res.append(tid)
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followlist[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followlist[followerId]:
            self.followlist[followerId].remove(followeeId)
