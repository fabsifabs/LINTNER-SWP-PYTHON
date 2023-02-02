from verketteteListe import verkettList, listElement
import random

def main():
    myList = verkettList()
    for i in range(20):
        myList.addLast(listElement(random.randrange(1,500)))
    

    print(myList)
    myList.heapSort()
    print(myList)
    myList.insertAtIndex(3,listElement(20))
    myList.insertAtIndex(6,listElement(22))
    print(myList)
    myList.heapSort()
    print(myList)
    myList.reverse()
    print(myList)

    myList.deleteAllAfter(5)
    myList.deleteAllAfter(6)
    print(myList)
    myList.addLast(listElement(200))
    print(myList)
    print(myList.elementIsInList(200))
    myList.deleteFirstElement(200)

    print("Shuffle:\n")
    print(myList)
    myList.shuffle()
    print(myList)
    myList.shuffle()
    print(myList)
    myList.shuffle()
    print(myList)
    
    

if __name__ == "__main__":
    main()