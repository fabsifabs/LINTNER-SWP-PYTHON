from arrayList import arrList
import random

def main():
    arr = arrList()

    for _ in range(500):
        arr.append(random.randrange(0,20))

    
    print(len(arr))
    print(arr)







if __name__ == "__main__":
    main()