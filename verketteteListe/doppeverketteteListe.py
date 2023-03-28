
class doppelListElement:
    def __init__(self, object):
        self.object = object
        self.nextElement = None
        self.prevElement = None

    def setNextElement(self, element):
        self.nextElement = element

    def getNextElement(self):
        return self.nextElement
    
    def setPrevElement(self,element):
        self.prevElement = element
    
    def getPrevElement(self):
        return self.prevElement

    def getObject(self):
        return self.object

    def setObject(self,ob):
        self.object = ob

    def __str__(self):
        return str(self.object)


class doppeltVerketteList:

    def __init__(self):
        self.firstElement = None
        self.lastElement = None
        self.elementCount = 0
        
    

    def __iter__(self):
        return self

    
    def __next__(self):
        if self.iteration.getNextElement() != None:
            self.iteration = self.iteration.getNextElement()
            return self.iteration
        else: 
            self.iteration = self.firstElement
            raise StopIteration

    def __len__(self):
        return self.elementCount

    def getLast(self):
        return self.lastElement

    def addLast(self,object):
        self.elementCount += 1
        if self.firstElement == None:
            self.firstElement = object
            self.lastElement = object
            self.iteration = self.firstElement
            return
        
        e = self.getLast()
        e.setNextElement(object)
        self.lastElement = object
        object.setPrevElement(e)
        

    def getElOnI(self,index):
        if index < self.elementCount//2:
            e = self.firstElement
            count = 0
            while e!= None:
                if count == index:
                    return e
                else:
                    count += 1
                    e = e.getNextElement()
                    
        else:
            e = self.lastElement
            count = 0 
            while e != None:
                if  self.elementCount - count - 1 == index:
                    return e
                else:
                    count += 1
                    e = e.getPrevElement()
                    

    def getValueOnI(self,index):
        if index < self.elementCount//2:
            e = self.firstElement
            count = 0
            while e!= None:
                if count == index:
                    return e.getObject()
                else:
                    count += 1
                    e = e.getNextElement()
                    
        else:
            e = self.lastElement
            count = 0 
            while e != None:
                if  self.elementCount - count-1 == index:
                    return e.getObject()
                else:
                    count += 1
                    e = e.getPrevElement()

    def __getitem__(self, index):
        return self.getElOnI(index)

    def pop(self,index):
        if index > self.elementCount-1:
            raise Exception("ERROR: index out of range")
        
        if index == 0:
            self.elementCount-=1
            res = self[index]
            self[index+1].setPrevElement(None)
            self.firstElement = self[index+1]
            return res
        
        if index == self.elementCount-1:
            
            res = self[index]
            
            self[index-1].setNextElement(None)
            self.lastElement = self[index-1]            
            self.elementCount-=1
            return res
        
        res = self[index]

        self[index-1].setNextElement(self[index+1])
        self[index].prevElement=self[index-1]
        self.elementCount-=1

        return res
            
    
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

    def shuffle(self):
        import random
        count = 0 
        rounds = random.randrange(50,100)
        while count <= rounds:
            count +=1
            self.swapTwoElements(random.randrange(0,self.elementCount),random.randrange(0,self.elementCount))

    def insertAtIndex(self,index, object):
        if index >= self.elementCount or index <0:
            raise Exception("ERROR: index out of range")

        self.elementCount+=1
        self[index].setPrevElement(object)
        object.setNextElement(self[index])
        object.setPrevElement(self[index-1])

        self[index-1].setNextElement(object)

        if index == self.elementCount-1:
            self.lastElement = object
        if index == 0:
            self.firstElement = object

    def insertAfter(self,place, object):
        e = self.firstElement
        while e != None:
            if e.getObject() == place:
                self.elementCount+=1
                s = e.getNextElement()
                e.setNextElement(object)
                s.setPrevElement(object)
                object.setNextElement(s)
                object.setPrevElement(e)
                return
            e = e.getNextElement()

        print("Not Found")
    
    def deleteAtIndex(self, index):
        if index > self.elementCount-1:
            raise Exception("ERROR: index out of range")
        
        if index == 0:
            self.elementCount-=1
            self[index+1].setPrevElement(None)
            self.firstElement = self[index+1]

        
        if index == self.elementCount-1:         
            self[index-1].setNextElement(None)
            self.lastElement = self[index-1]            
            self.elementCount-=1
        
        self[index-1].setNextElement(self[index+1])
        self[index].prevElement=self[index-1]
        self.elementCount-=1


    def deleteFirstElement(self, object):
        e = self.firstElement
        while e!= None:
            if e.getObject() == object:
                self.elementCount -= 1
                if e.getNextElement() == None:
                    e.getPrevElement().setNextElement(None)
                    self.lastElement = e.getPrevElement()
                    e.setPrevElement(None)
                    return 
                if e.getPrevElement() == None:
                    self.firstElement = e.getNextElement()
                    e.getNextElement().setPrevElement(None)
                    return
                s = e.getNextElement()
                p = e.getPrevElement()
                e.getPrevElement().setNextElement(e.getNextElement())
                p.setNextElement(s)
                return

            e = e.getNextElement()
        print("Not Found")

    def deleteElementAndAllAfter(self, object):
        e = self.firstElement
        while e != None:
            if e.getObject() == object:
                e.setNextElement(None)
                self.lastElement = e.getPrevElement()
                self.updateCount()
                return 
            e = e.getNextElement()
        print("Not Found")

    def deleteAllAfter(self, object):
        e = self.firstElement
        while e != None:
            if e.getObject() == object:
                
                e.setNextElement(None)
                self.lastElement = e

                return 
            e = e.getNextElement()
        print("Not Found")

    def deleteAll(self):
        self.firstElement = None
        self.lastElement = None
        self.elementCount = 0

    def deleteAllElements(self, object):
        for i in range(0,self.elementCount):
            e = self[i]

        for e in self:
            if e.getObject() == object:
                if e.getPrevElement() == None:
                    n = e.getNextElement()
                    n.setPrevElement(None)
                    self.firstElement = n
                elif e.getNextElement()== None:
                    p = e.getPrevElement()
                    p.setNextElement(None)
                    self.lastElement = p
                else:
                    p = e.getPrevElement()
                    n = e.getNextElement()
                    p.setNextElement(n)
                    n.setPrevElement(p)

        self.updateCount()

    def updateCount(self):
        self.elementCount = 1
        for i in self:
            self.elementCount += 1

    def elementIsInList(self,object):
        e = self.firstElement
        while e != None:
            if e.getObject() == object:
                return True
            e = e.getNextElement()
        return False


    def countOcc(self,object):
        count = 0
        e = self.firstElement
        while e != None:
            if e.getObject() == object:
                count += 1

            e = e.getNextElement()
        return count
    
    def deleteDup(self):
        unique = set()
        cur = self.firstElement
        prev = None

        while cur != None:
            if cur.getObject() in unique:
                p = cur.getPrevElement()
                n = cur.getNextElement()
                p.setNextElement(n)
                n.setPrevElement(p)
            else:
                unique.add(cur.getObject())
                prev = cur

            cur = prev.getNextElement()
        
        self.updateCount()

    def __str__(self):
        e = self.firstElement
        result = "["
        while e != None:
            result += str(e)
            if e.getNextElement() != None:
                result += ", "
            e = e.getNextElement()


        result += "]"
        return result





