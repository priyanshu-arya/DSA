import random
def rlist(li=random.randint(1,100)):
    randomlist = []
    for i in range(0,li):
        n = random.randint(1,1000)
        randomlist.append(n)
    return randomlist

#print(rlist())