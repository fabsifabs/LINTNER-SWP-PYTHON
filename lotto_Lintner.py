import random

def getNumber():
    a=[]
    for i in range(46):
        a.append(i)
    for i in range(0,6):
        x = random.randint(0,44-i)
        a[x],a[45-i] = a[45-i],a[x]

    return a[-6:]


d = []

for i in range(100000):
  d = d + getNumber()


for i in range(1,46):
    print(i,":",d.count(i))