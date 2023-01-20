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

    def __str__(self):
        return str(self.object)


class verkettList:

    def __init__(self):
        self.firstElemet = listElement(None)
        self.elementCount = 0

    def getLast(self):
        e = self.firstElemet

        while e.getNextElement() != None:
            e = e.getNextElement()

        return e

    def addLast(self,object):
        e = self.getLast()
        e.setNextElement(object)
        self.elementCount += 1


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
                    return 
            e = e.getNextElement()
        print("Not Found")

    def deleteAllAfter(self, object):
        e = self.firstElemet
        while e != None:
            if e.getObject() == object:
                    e.setNextElement(None)
                    return 
            e = e.getNextElement()
        print("Not Found")

    def deleteAll(self):
        self.firstElemet.setNextElement(None)

    def deleteAllElements(self, object):
        e = self.firstElemet
        noneFound = True
        while e.getNextElement() != None:
            if e.getNextElement().getObject() == object:
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





