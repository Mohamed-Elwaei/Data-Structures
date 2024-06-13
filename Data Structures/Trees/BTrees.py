class Node:
    def __init__(self,leaf=False) -> None:
        self.keys=[]
        self.chilren=[]



class BTree(Node):
    def __init__(self,t):
        self.root=Node(True)
        self.t=t

    def search(self,k,node=None):
        node=self.root if not node else node
        i=0

        while i<len(node.keys) and node.keys[i]<k:
            i+=1
        
        if i<len(node.keys) and node.keys[i]==k:
            return (node,i)
        
        elif node.leaf:
            return None
        else:
            return self.search(k, node.chilren[i])
        
    
    def split_child(self,x,i):

        t=self.t

        y=x.children[i] # y is a full node


        z=Node(y.leaf)

        x.keys.insert(i,y.keys[t-1]) #insert the median
        x.children.insert(i+1, z) # make z a child of x


        z.keys=y[t:2*t - 1]
        y.keys=y.keys[:t-1]


        if not y.leaf:
            z.children=y[t:2*t]
            y.children=y.children[0:t-1]



    def insert(self, k):
        t=self.t
        root=self.root

        if (root.keys) == 2*t -1:
            new_root=Node()
            self.root=new_root
            new_root.chilren.insert(0,root)
            self.split_child(new_root, 0)
            self.insert_nonfull(new_root, k)
        self.insert_nonfull(root,k)

    def insert_nonfull(self, node, k):

        t=self.t
        i=len(node.keys)-1

        if node.leaf:
            node.append(None)
            while i>=0 and k<node.keys[i]:
                node.keys[i+1]=node.keys[i]
                i-=1
            i+=1
            node.keys[i]=k
        
        else:
            while i>=0 and k<node.keys[i]:
                i-=1
            i+=1
            if len(node.children[i].keys)==2*t -1 :
                self.split_child(node,i)
                if k>self.keys[i]:
                    i+=1
            self.insert_nonfull(node.children[i],k)
