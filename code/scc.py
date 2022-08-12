from user import User
class scc:
    def __init__(self,graph) -> None:
        self.N=len(graph)
        self.stack=[]
        self.graph=graph
        self.totalNumberOfSCC=0

        self.visitedPushIntoStack={}
        
        for i in graph:
            self.visitedPushIntoStack[i]=False
        self.visitedPopFromStack={}
        for i in graph:
            self.visitedPopFromStack[i]=False
    
    def fillInStack(self,v,visited):
        visited[v]=True
        for i in v.follower:
            if visited[i]==False:
                self.fillInStack(i,visited)
        self.stack.append(v)
    def popFromStack(self,v,visited):
        visited[v]=True
        print(v.uid)
        for i in v.follower:
            if visited[i]==False:
                self.popFromStack(i,visited)
    def solve(self):
        for i in self.graph:
            if self.visitedPushIntoStack[i]==False:
                self.fillInStack(i,self.visitedPushIntoStack)
        print([i.uid for i in self.stack])
        for i in self.stack:
            i.follower,i.following=i.following,i.follower
        while self.stack:
            v=self.stack.pop()
            if self.visitedPopFromStack[v]==False:
                self.popFromStack(v,self.visitedPopFromStack)
                print("")
                self.totalNumberOfSCC+=1
        print(f'Total number of SCC: {self.totalNumberOfSCC}')


            
        
    