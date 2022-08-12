from user import User
class scc:
    def __init__(self,graph) -> None:
        self.N=len(graph)
        self.stack=[]
        self.graph=graph
        self.totalNumberOfSCC=0
        self.influencers=[]
        self.temp=set()

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
        self.temp.add(v)
        for i in v.follower:
            if visited[i]==False:
                self.popFromStack(i,visited)
    
    def solve(self):
        for i in self.graph:
            if self.visitedPushIntoStack[i]==False:
                self.fillInStack(i,self.visitedPushIntoStack)
        #print([i.uid for i in self.stack])
        for i in self.stack:
            i.follower,i.following=i.following,i.follower
        while self.stack:
            v=self.stack.pop()
            if self.visitedPopFromStack[v]==False:
                self.temp=set()
                self.popFromStack(v,self.visitedPopFromStack)
                check=set()
                for i in self.temp:
                    check=check.union(i.follower)

                #print(f'the temp is {self.temp}')
                #print(f'the check is {check}')
                if self.temp==check or len(check)==0:
                    self.totalNumberOfSCC+=1
                    influencer=max(list(self.temp),key=lambda x:len(x.follower))
                    self.influencers.append(influencer.uid)
        return self.influencers
                
                
                
        


            
        
    