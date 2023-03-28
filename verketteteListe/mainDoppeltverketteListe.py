from doppeverketteteListe import doppelListElement as dE, doppeltVerketteList as dV
import random

def main():
    myList = dV()
    for i in range(10):
        myList.addLast(dE(random.randrange(1,20)))

    print(myList)

    print(myList.deleteDup())
    
    print(myList.elementCount)
    
    for i in range(0,myList.elementCount):
        print(myList.getElOnI(i), end =" ")





if __name__ == "__main__":
    main()