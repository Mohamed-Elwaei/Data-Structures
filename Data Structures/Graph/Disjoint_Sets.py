class UnionFind:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size <= 0 is not allowed")
        
        self.size = self.numComponents = size
        self.sz = [1] * size
        self.id = list(range(size))
        
    def find(self, p):
        if p==self.id[p]: return p
        else:
             self.id[p]=self.find(self.id[p])
             return self.id[p]

    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def componentSize(self, p):
        return self.sz[self.find(p)]
    
    def size(self):
        return self.size
    
    def components(self):
        return self.numComponents
    
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        
        if root1 == root2:
            return
        
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        
        self.numComponents -= 1




class UnionFind:
    def __init__(self,size) -> None:
        self.size=self.components=size
        self.sz=[1]*size
        self.ids=[n for n in range(size)]

    def find(self, p):
        if p==self.ids[p]: return p
        else: 
            self.ids[p]=self.find(self.ids[p])
            return self.ids[p]
    def unify(self, x, y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x==root_y:
            return
        
        if root_y>root_x:
            self.sz[root_y]+=self.sz[root_x]
            self.ids[root_x]=root_y
        else:
            self.sz[root_x]+=self.sz[root_y]
            self.ids[root_y]=root_x

        self.components-=1
    def connected(self, x,y):
        return self.find(x)==self.find(y)

# Create a UnionFind instance with 10 elements (0 to 9)
uf = UnionFind(10)

# Perform some union operations
uf.unify(0, 2)
uf.unify(1, 8)
uf.unify(3, 5)
uf.unify(7, 9)
uf.unify(3, 7)

# Check if elements are connected
print(uf.connected(0, 2))  # Output: True
print(uf.connected(1, 5))  # Output: False

# Get the size of the component/set for an element
print(uf.components)  # Output: 5

# Get the total number of elements in the UnionFind
print(uf.size)  # Output: 10

# Get the number of remaining components/sets
print(uf.components)  # Output: 5
