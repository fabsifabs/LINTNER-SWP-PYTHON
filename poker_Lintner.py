import random

cards = [i for i in range(52)]
hands = ["royal flush","straight flush","four of a kind","full house","flush","straight","three of a kind","two pairs","pair","high card"]
#print(cards)
drawCount = 5

occHand = [0]*10

def draw():
    random.shuffle(cards)
    d = cards[:5]
    d.sort()
    #print(d)
    return d

def checkHand(dC):
    colArr = []
    for x in dC:
        colArr.append(x//13)

    numArr = []
    for x in dC:
        numArr.append(x%13)

    occ = numArr.count(max(numArr, key=numArr.count))

    if len(set(colArr))==1:
        if numArr[0]==8 and numArr[4]==12:
            occHand[0]+=1   #royal flush
        elif numArr[0]-numArr[4]==-4:
            occHand[1] += 1 #straight flush
        else:
            occHand[4] += 1 #flush

    elif numArr[0]-numArr[4]==-4 and occ == 1:#straight
        occHand[5] += 1
    elif occ == 4: #four of a kind
        occHand[2] += 1
    elif occ == 3 and len(set(numArr))==2:
        occHand[3] += 1 #fullhouse
    elif occ == 3:
        occHand[6] += 1 #three of a kind
    elif occ == 2 and len(set(numArr))==3:
        occHand[7] += 1 #two pairs
    elif occ == 2:
        occHand[8] += 1 #pair
    else:
        occHand[9]+=1 #high cards




def playCards(draws):
    for i in range(draws):
        checkHand(draw())

    print("Draws:",draws)
    print("sum",sum(occHand))
    for i in range(0,10):
        print("Absolute Occurences:",occHand[i]," \t|| Relative:", occHand[i]/draws," \t|| ",hands[i])




if __name__ == "__main__":
    playCards(500000)


