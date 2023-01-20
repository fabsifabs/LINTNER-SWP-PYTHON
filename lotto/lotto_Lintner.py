import random

def draw(min,max, numbersPerDraw):
    a=[]
    for i in range(max+1):
        a.append(i)

    for i in range(min-1,numbersPerDraw):
        x = random.randint(0,max-min-1-i)
        a[x],a[max-min-i] = a[max-min-i],a[x]

    return a[-numbersPerDraw:]

def drawALot(drawCount,min,max, numbersPerDraw ):
    d = []
    for i in range(drawCount):
      d = d + draw(min,max,numbersPerDraw)

    return d

for i in range(0,45):
    print(i+1,":",drawALot(100000,20,50,6).count(i) )