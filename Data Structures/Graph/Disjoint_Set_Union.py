from random import randint

class DisjointSet:

    def __init__(self, size):
        self.size=size
        self.parents=list(range(size))
        self.ranks=[0] * size


    def make_set(self, x):
        self.parents[x]=x
        self.ranks[x]=randint(1, self.size)

    def find(self, x):
        if x!=self.parents[x]:
            self.parents[x]=self.find(self.parents[x])
        return x
    
    def union(self, x, y):
        x,y=self.find(x),self.find(y)

        if x!=y:
            if (self.ranks[x] < self.ranks[y]):
                y,x=x,y
            self.parents[y]=x



# Create a disjoint set of size 6
dsu = DisjointSet(6)

# Make set for each element
for i in range(6):
    dsu.make_set(i)

# Perform some union operations
dsu.union(0, 1)
dsu.union(2, 3)
dsu.union(4, 5)
dsu.union(1, 3)
dsu.union(0, 5)

# Find representatives of some elements
print(dsu.find(2))  # Output: 2
print(dsu.find(4))  # Output: 4
print(dsu.find(1))  # Output: 0 (after union operation)

