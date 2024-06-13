class Node:
    def __init__(self,val=0,left=None,right=None,bf=0,height=0):
        self.val=val
        self.left=left
        self.right=right
        self.bf=bf
        self.height=height




class AVL(Node):
    def __init__(self,root=None):
        self.root=root

    def __update(self,node):
        lh= -1 if not node.left else node.left.height
        rh= -1 if not node.right else node.right.height

        node.height=1+max(lh,rh)
        node.bf=rh-lh

    
    def __rightRotate(self,node):
        New_P=node.left
        node.left=New_P.right
        New_P.right=node
        self.__update(node)
        self.__update(New_P)
        return New_P

    def __leftRotate(self,node):
        New_P=node.right
        node.right=New_P.left
        New_P.left=node
        self.__update(node)
        self.__update(New_P)
        return New_P



    def insert(self,val):
        self.root=self.__insert(self.root,val)

    def remove(self,val):
        self.root=self.__remove(self.root,val)

    def __remove(self, root, val):
        if not root:
            return root

        elif root.val > val:
            root.left = self.__remove(root.left, val)
        elif root.val < val:
            root.right = self.__remove(root.right, val)
        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.__remove(root.right, root.val)

        self.__update(root)
        return self.__balance(root)


            

    def __insert(self,root,val):

        if root==None:
            return Node(val)
        
        elif root.val==val:
            return None
        
        elif root.val<val:
            root.right=self.__insert(root.right,val)
       
        elif root.val>val:
            root.left=self.__insert(root.left,val)

        self.__update(root)

        return self.__balance(root)
    
    
    
    def __balance(self,node):
        #Left Heavy
        if node.bf==-2:
            #Left left case
            if node.left.bf<=0:
                return self.__rightRotate(node)
            #Left right case
            else:
                return self.__leftRightCase(node)
        #Right Heavy
        elif node.bf==2:
            if node.right.bf>=0:
                return self.__leftRotate(node)
            else:
                return self.__rightLeftCase(node)
        return node
    

    def __leftRightCase(self,node):
        node.left=self.__leftRotate(node.left)
        
        return self.__rightRotate(node)

    def __rightLeftCase(self,node):
        node.right=self.__rightRotate(node.right)

        return self.__leftRotate(node)
    



    
            
        


def draw_avl_tree(node, level=0, indent=4):
    if node is None:
        return
    
    draw_avl_tree(node.right, level + 1, indent)
    print(" " * (level * indent) + str(node.val))
    draw_avl_tree(node.left, level + 1, indent)



avl = AVL()
for i in range(16):
    avl.insert(i)




draw_avl_tree(avl.root)

avl.remove(1)
avl.remove(2)
avl.remove(3)
avl.remove(0)
avl.remove(9)
print('\n\n')


draw_avl_tree(avl.root)

