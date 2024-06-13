import math
class SparseTable:

    def __init__(self, arr, func):

        self.N=len(arr)
        self.k=int(math.log2(self.N))+1
        self.sp=[[0 for _ in range(self.N)] for _ in range(self.k)]
        self.func=func

        for i in range(self.N):
            self.sp[0][i]=arr[i]


        for i in range(1, self.k +1):
            j=0
            while j + (1<<i) <=self.N:
                left=self.sp[i-1][j]
                right=self.sp[i-1][j + (1<<(i-1))]
                self.sp[i][j]=func(left,right)

                j+=1

    
    def query(self, L, R):
        ans=1
        for i in range(self.k, -1, -1):
            if (1 << i) <= R - L + 1:
                ans =self.func(ans,self.sp[i][L])
                L += 1 << i
        return ans

                

# Define the associative function
def func(a, b):
    return a * b  # Sum function

# Create an instance of SparseTable
arr = [1, 2, 3, 4, 5, 6, 7, 8]
sparse_table = SparseTable(arr, min)

# Perform queries
result1 = sparse_table.query(2, 5)
print("Query 1 result:", result1)  # Expected output: 14 (sum of elements from index 2 to 5)

result2 = sparse_table.query(0, 7)
print("Query 2 result:", result2)  # Expected output: 36 (sum of all elements)

result3 = sparse_table.query(4, 6)
print("Query 3 result:", result3)  # Expected output: 18 (sum of elements from index 4 to 6)
