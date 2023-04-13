class arrList:

    def __init__(self) -> None:
        self.array = [None]*10
    
    
    def __len__(self):
        res = 0
        for e in self.array:
            if e == None:
                break
            else:
                res+=1
                      
        return res


    def __iter__(self):
        self.n = 0
        return self
    

    def __next__(self):
        if self.n <=len(self)-1:
            res = self.array[self.n]
            self.n+=1
            return res
        else:
            self.n = 0
            raise StopIteration


    def __getitem__(self, index):
        return self.array[index]   


    def append(self, object):
        for i in range(0,len(self)+1):
            try:
                if self.array[i] == None:
                    self.array[i] = object
                    return
            except IndexError:
                pass

        
        newArr = [None]*(len(self)*2)

        for i in range(0,len(self)):
            newArr[i] = self.array[i]

        self.array = newArr
        self.append(object)


    def __str__(self):
        result = "["
        for i in range(0,len(self)):
            result += str(self.array[i])
            if i != len(self)-1:
                result += ", "
        result += "]"
        return result