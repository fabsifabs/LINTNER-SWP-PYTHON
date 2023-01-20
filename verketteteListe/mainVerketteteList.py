from verketteteListe import verkettList, listElement


def main():
    myList = verkettList()
    myList.addLast(listElement("1"))
    myList.addLast(listElement("1"))
    myList.addLast(listElement("3"))
    myList.addLast(listElement("4"))
    myList.addLast(listElement("5"))
    myList.addLast(listElement("6"))
    myList.addLast(listElement("7"))


    print(myList)
    myList.insertAfter("1",listElement("33"))
    myList.insertAfter("33",listElement("23"))
    print(myList)

    arr = [1,2,3,4,5]
    print(arr)
    



if __name__ == "__main__":
    main()