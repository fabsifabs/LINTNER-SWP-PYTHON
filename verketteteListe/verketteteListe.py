class listElement:
    def __init__(self, object):
        self.object = object
        self.nextElement = None

    def setNextElement(self, element):
        self.nextElement = element

    def getNextElement(self):
        return self.nextElement

    def getObject(self):
        return self.object

    def setObject(self,ob):
        self.object = ob

    def __str__(self):
        return str(self.object)


class verkettList:

    def __init__(self):
        self.firstElemet = listElement(None)
        self.elementCount = 0
        self.iteration = self.firstElemet

    

    def __iter__(self):
        return self

    

    def __next__(self):
        if self.iteration.getNextElement() != None:
            self.iteration = self.iteration.getNextElement()
            return self.iteration
        else: 
            self.iteration = self.firstElemet
            raise StopIteration


    def getLast(self):
        e = self.firstElemet
        while e.getNextElement() != None:
            e = e.getNextElement()

        return e

    def addLast(self,object):
        self.elementCount += 1
        e = self.getLast()
        e.setNextElement(object)

    def getElOnI(self,index):
        e = self.firstElemet
        count = 0
        while e.getNextElement() != None:
            if count == index:
                return e.getNextElement()
            else:
                count += 1
                e = e.getNextElement()

    def getValueOnI(self,index):
        e = self.firstElemet
        count = 0
        while e.getNextElement() != None:
            if count == index:
                return e.getNextElement().getObject()
            else:
                count += 1
                e = e.getNextElement()

    def pop(self,index):
        e = self.firstElemet
        count = 0
        while e.getNextElement() != None:
            if count == index:
                result = e.getNextElement().getObject()
                self.elementCount -= 1
                if e.getNextElement().getNextElement() != None:
                    e.setNextElement(e.getNextElement().getNextElement())
                else:
                    e.setNextElement(None)

                return result

            count += 1
            e = e.getNextElement()

        raise Exception("ERROR: index out of range")
    
    def swapTwoElements(self, x,y):
        save = self.getValueOnI(x)
        self.getElOnI(x).setObject(self.getValueOnI(y))
        self.getElOnI(y).setObject(save)
    
    def heapSort(self):
        def heapify(n, i):
            largest = i 
            l = 2 * i + 1 
            r = 2 * i + 2 
            
            if l < n and self.getValueOnI(i) < self.getValueOnI(l):
                largest = l

            if r < n and self.getValueOnI(largest) < self.getValueOnI(r):
                largest = r

            if largest != i:
                self.swapTwoElements(i,largest)
                heapify(n, largest)

        n = self.elementCount

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.swapTwoElements(i,0)
            heapify(i, 0)
    
    def reverse(self):
        size = self.elementCount
        if(size==1):
            return
        elif(size==2):
            self.swapTwoElements(1,0)
            return 
        
        else:
            i=0
            while(i<size//2):
                self.swapTwoElements(i, size-i-1)
                i+=1
            return 


    def insertAtIndex(self,index, object):
        e = self.firstElemet
        count = 0
        while e != None:
            if count == index:
                self.elementCount += 1
                save = e.getNextElement()
                e.setNextElement(object)
                object.setNextElement(save)
                return

            count += 1
            e = e.getNextElement()
        
        raise Exception("ERROR: index out of range")

    def insertAfter(self,place, object):
        e = self.firstElemet
        while e != None:
            if e.getObject() == place:
                
                save = e.getNextElement()
                e.setNextElement(object)
                object.setNextElement(save)
                return
            e = e.getNextElement()

        print("Not Found")
            

    def deleteFirstElement(self, object):
        e = self.firstElemet
        while e.getNextElement() != None:
            if e.getNextElement().getObject() == object:
                self.elementCount -= 1
                if e.getNextElement().getNextElement() != None:
                    e.setNextElement(e.getNextElement().getNextElement())
                    return 
                else:
                    e.setNextElement(None)
                    return 
                
            e = e.getNextElement()
        print("Not Found")

    def deleteElementAndAllAfter(self, object):
        e = self.firstElemet
        while e.getNextElement() != None:
            if e.getNextElement().getObject() == object:
                    e.setNextElement(None)
                    self.updateCount()
                    return 
            e = e.getNextElement()
        print("Not Found")

    def deleteAllAfter(self, object):
        e = self.firstElemet
        while e != None:
            if e.getObject() == object:
                    e.setNextElement(None)
                    self.updateCount()
                    return 
            e = e.getNextElement()
        print("Not Found")

    def deleteAll(self):
        self.firstElemet.setNextElement(None)
        self.elementCount = 0

    def deleteAllElements(self, object):
        e = self.firstElemet
        noneFound = True
        while e.getNextElement() != None:
            if e.getNextElement().getObject() == object:
                self.updateCount()
                if e.getNextElement != None and e.getNextElement().getNextElement() != None:
                    e.setNextElement(e.getNextElement().getNextElement())
                    noneFound = False
                else:
                    e.setNextElement(None)
                    noneFound = False
                    
                    return
                    
                if noneFound == False:
                    self.deleteAllElements(object)

            e = e.getNextElement()

    def updateCount(self):
        self.elementCount = 0
        for i in self:
            self.elementCount += 1

    def elementIsInList(self,object):
        e = self.firstElemet
        while e != None:
            if e.getObject() == object:
                return True
            e = e.getNextElement()
        return False


    def countOcc(self,object):
        count = 0
        e = self.firstElemet
        while e != None:
            if e.getObject() == object:
                count += 1

            e = e.getNextElement()
        return count
    
    def deleteDup(self):
        unique = set()
        cur = self.firstElemet
        prev = None

        while cur != None:
            if cur.getObject() in unique:
                prev.setNextElement(cur.getNextElement())

            else:
                unique.add(cur.getObject())
                prev = cur

            cur = prev.getNextElement()
        
        self.updateCount()

    def __str__(self):
        e = self.firstElemet
        result = "["
        while e != None:
            result += str(e)
            if e.getNextElement() != None:
                result += ", "
            e = e.getNextElement()


        result += "]"
        return result





