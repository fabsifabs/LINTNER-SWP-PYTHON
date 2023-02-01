from verketteteListe import verkettList, listElement


def main():
    myList = verkettList()
    myList.addLast(listElement(1))
    myList.addLast(listElement(6))
    myList.addLast(listElement(11))
    myList.addLast(listElement(4))
    myList.addLast(listElement(3))
    myList.addLast(listElement(1))
    myList.addLast(listElement(14))
    myList.addLast(listElement(2))

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
    print(myList)
    

if __name__ == "__main__":
    main()