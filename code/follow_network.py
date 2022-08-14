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
    #function to fill in the stack
    def _fill_in_stack(self, v, visited):
        visited[v] = True
        for i in v.follower:
            if not visited[i]:
                self._fill_in_stack(i, visited)
        self.stack.append(v)
    #function to pop from the stack after we finsihed with searching and reversing the graph
    def _pop_from_stack(self, v, visited):
        visited[v] = True
        self.temp.add(v)
        for i in v.follower:
            if not visited[i]:
                self._pop_from_stack(i, visited)

    def solve(self):
        #start dfs to push all node into the stack
        for i in self.graph:
            if not self.visitedPushIntoStack[i]:
                self._fill_in_stack(i, self.visitedPushIntoStack)
        #reverse the graph
        for i in self.stack:
            i.follower, i.following = i.following, i.follower
        #start dfs to pop all node from the stack and calculate the SCC
        while self.stack:
            v = self.stack.pop()
            #if the node is visited, we skip
            if not self.visitedPopFromStack[v]:
                #create a set to record the SCC from current node
                self.temp = set()
                self._pop_from_stack(v, self.visitedPopFromStack)
                #check set is used to find if there is other nodes pointing to the current SCC group
                check = set()
                #union all the connecting nodes in the SCC group
                for i in self.temp:
                    check = check.union(i.follower)
                #if there is no other nodes pointing to the current SCC group, we add it to the list of influencers
                if self.temp == check or (not check):
                    self.total_num_of_influencers += 1
                    #we pick the user who has most followers as representative of the SCC group
                    influencer = max(list(self.temp), key=lambda x: len(x.follower))
                    self.influencers.append(influencer.uid)

        for i in self.graph:
            i.follower, i.following = i.following, i.follower

        return self.influencers
