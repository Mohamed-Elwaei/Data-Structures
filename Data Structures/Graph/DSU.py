from random import randint

class DisjointSet:

    def __init__(self, size):
        self.size=size
        # Hashmap
        #Each index is a key (node). And the value is the parent
        self.parents=list(range(size))
   


    def make_set(self, x):

        self.parents[x]=x

    def find(self, x):
        #Path compression 
        if x!=self.parents[x]:
            self.parents[x]=self.find(self.parents[x])
        return x
    
    def union(self, x, y):


        x,y=self.find(x),self.find(y)

        # if x and y are not part of the same set, union them
        if x!=y:
            self.parents[y]=x

