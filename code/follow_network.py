class FollowNetwork:
    def __init__(self, graph) -> None:
        self.N = len(graph)
        self.stack = []
        self.graph = graph
        self.total_num_of_influencers = 0
        self.influencers = []
        self.temp = set()

        self.visitedPushIntoStack = {}

        for i in graph:
            self.visitedPushIntoStack[i] = False
        self.visitedPopFromStack = {}
        for i in graph:
            self.visitedPopFromStack[i] = False

    def _fill_in_stack(self, v, visited):
        visited[v] = True
        for i in v.follower:
            if not visited[i]:
                self._fill_in_stack(i, visited)
        self.stack.append(v)

    def _pop_from_stack(self, v, visited):
        visited[v] = True
        self.temp.add(v)
        for i in v.follower:
            if not visited[i]:
                self._pop_from_stack(i, visited)

    def solve(self):
        for i in self.graph:
            if not self.visitedPushIntoStack[i]:
                self._fill_in_stack(i, self.visitedPushIntoStack)
        for i in self.stack:
            i.follower, i.following = i.following, i.follower
        while self.stack:
            v = self.stack.pop()
            if not self.visitedPopFromStack[v]:
                self.temp = set()
                self._pop_from_stack(v, self.visitedPopFromStack)
                check = set()
                for i in self.temp:
                    check = check.union(i.follower)
                if self.temp == check or (not check):
                    self.total_num_of_influencers += 1
                    influencer = max(list(self.temp), key=lambda x: len(x.follower))
                    self.influencers.append(influencer.uid)

        for i in self.graph:
            i.follower, i.following = i.following, i.follower

        return self.influencers
