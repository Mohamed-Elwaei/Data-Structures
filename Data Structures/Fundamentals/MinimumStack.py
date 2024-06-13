class MinStack(object):

    def __init__(self):
        self.st=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        min_val=val if len(self.st)==0 else min(self.st[-1][-1],val)

        self.st.append((val,min_val))      
        

    def pop(self):
        """
        :rtype: None
        """
        self.st.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.st[-1][1]