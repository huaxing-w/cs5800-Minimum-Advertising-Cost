class User:
    def __init__(self, uid: int) -> None:
        self.uid = uid
        self.following = set()
        self.follower = set()
    def followOne(self, other: 'User') -> None:
        self.following.add(other)
        other.follower.add(self)
    def unfollowOne(self, other: 'User') -> None:
        if other in self.following:
            self.following.remove(other)
            other.follower.remove(self)
    def removeOneFollower(self, other: 'User') -> None:
        if other in self.follower:
            self.follower.remove(other)
            
        
    def __repr__(self) -> str:
        return f'User id: {self.uid}\n Following: {[f.uid for f in self.following]}\n Followers: {[e.uid for e in self.follower]}'
    def __str__(self) -> str:
        return f'User id: {self.uid}\n Following: {[f.uid for f in self.following]}\n Followers: {[e.uid for e in self.follower]}'
    def __eq__(self, other) -> bool:
        return self.uid == other.uid
    def __hash__(self) -> int:
        return hash(self.uid)




    

    