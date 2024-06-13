# class FenwickTree:
#     def __init__(self, n):
#         self.size = n
#         self.tree = [0] * (n + 1)

#     def update(self, index, delta):
#         while index <= self.size:
#             self.tree[index] += delta
#             index += index & -index

#     def query(self, index):
#         result = 0
#         while index > 0:
#             result += self.tree[index]
#             index -= index & -index
#         return result

#     def range_query(self, left, right):
#         return self.query(right) - self.query(left - 1)


class FenwickTree:

    def __init__(self, A):
        self.n=len(A)
        self.bit=[0] * self.n

        for i in range(self.n):
            self.bit[i]+=A[i]
            r= i | (i+1)
            if r < self.n:
                self.bit[r]+=self.bit[i]

    def prefixSum(self, r):
        g=lambda a: a & (a + 1)
        ret=0
        while r>=0:
            ret+=self.bit[r]
            r=g(r) -1
        return ret
    def prefixSum(self, r):
        g=lambda a: a & (a + 1)
        ret=0
        while r>=0:
            ret+=self.bit[r]
            r=g(r) -1
        return ret
    

    def sum(self,l, r):
        return self.prefixSum(r) - self.prefixSum(l-1)
    
    def add(self, idx, delta):

        while idx<self.n:
            self.bit[idx]+=delta
            idx= idx | (idx + 1)


            

# tree = FenwickTree(5)
# tree.update(2, 3)
# tree.update(4, 2)
# print(tree.query(5))  # Output: 5
# print(tree.range_query(2, 4))  # Output: 5


# Create a Fenwick tree with size 5


A=[5,2,9,-3,5,20,10,-7,2,3,-4,0,-2,15,5]

tree = FenwickTree(A)


print(tree.prefixSum(7), sum(A[:9]))