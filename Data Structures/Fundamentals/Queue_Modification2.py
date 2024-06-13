from collections import deque
added=[0]
removed=[0]
dq=deque([])


def get_min():
    return dq[0][0]


def insert(elem,dq):
    while dq and dq[-1][0]>elem:
        dq.pop()
    dq.append((elem,added[0]))
    added[0]+=1

def remove(dq):
    if dq and dq[0][1]==removed[0]:
        tmp=dq.pop()
    removed[0]+=1
    return tmp


dq=deque([])


tmp=[2,7,33,5,1,44,22]




