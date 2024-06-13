class Fenwick:
    def __init__(self,arr) -> None:
        self.n = len(arr)
        self.BIT = [0] * (self.n+1)

        for i in range(self.n):
            self.update(arr[i],i)
    

    def update(self,delta, index):

        index+=1

        while index<self.n+1:
            self.BIT[index] += delta

            index += (index & -index)
    
    def prefixSum(self,index):
        ret=0
        index+=1

        while index>0:
            ret+=self.BIT[index]
            index-=(index & -index)
        return ret
    
    def Sum(self,l,r):
        return self.prefixSum(r) - self.prefixSum(l)



A=[5,2,9,-3,5,20,10,-7,2,3,-4,0,-2,15,5]
B=[i for i in range(11)]
BIT=Fenwick(A)


BIT2=Fenwick(B)

for i in range(len(B)):
    print(BIT2.prefixSum(i) ,(i*(i+1))//2)
    print(BIT2.Sum(i-1,i))