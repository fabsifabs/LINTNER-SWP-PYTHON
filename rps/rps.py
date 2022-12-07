import random, requests, json



def getInput():
    noCorrectAnswer = True
    while (noCorrectAnswer):
        noCorrectAnswer = False
        inputP = input("Choose between: 0/rock, 1/spock, 2/paper, 3/lizzard, 4/scissors, 5/exit:    ")
        playerInput = -1
        if((inputP.isdigit() and int(inputP) == 5)):

            print("exit")
            startGame()


        elif (inputP.isdigit()):
            if int(inputP) in [0,1,2,3,4]:
                return int(inputP)
            else:
                noCorrectAnswer = True
                print("not a availabe choice")
        else:
            inputP = inputP.lower()
            match inputP:
                case "rock":
                    return 0
                case "spock":
                    return 1
                case "paper":
                    return 2
                case "lizzard":
                    return 3
                case "scissors":
                    return 4
                case other:
                    noCorrectAnswer = True
                    print("not a availabe choice")

def toName(i):
    match i:
        case 0:
            return "rock"
        case 1:
            return "spock"
        case 2:
            return "paper"
        case 3:
            return "lizzard"
        case 4:
            return "scissors"


def checkResult(p, c):
   dif = (c-p)%5

   if dif ==0:
       return "draw"
   elif dif > 2:
       return "player won"
   else:
       return "Computer won"


def playARound(currentPlayer):
    playerChoice = getInput()
    compChoice = random.randrange(0,4)
    print("You chose: "+toName(playerChoice)+"\tComputer chose: "+toName(compChoice))
    print(checkResult(playerChoice,compChoice)+"\n")
    print(currentPlayer,toName(playerChoice))
    sendData(currentPlayer,toName(playerChoice))
    playARound(currentPlayer)

def startGame():
    inputP = input("Choose between (1/play), (2/data), (3/userData) or (4/exit):  ")
    if inputP.isdigit() and int(inputP) in [1,2,3]:
        inputP = int(inputP)
        match inputP:
            case 1:
                currentPlayer = input("playerName:  ").strip()
                playARound(currentPlayer)
            case 2:
                getData()
            case 3:
                inputP = input("Which user?")
                getUserData(inputP.strip())
            case 4:
                exit()
            case other:
                print("something went wrong!")


def sendData(playerName,symbol, url="http://127.0.0.1:5000"):
    data = {"Name":playerName,"Symbol": symbol,"Symbolanzahl":1}

    requests.put(url, json.dumps(data))

def getData(url="http://127.0.0.1:5000"):
    data = requests.get(url)
    print(data.json())

def getUserData(username, url="http://127.0.0.1:5000"):
    data = requests.get("{0}/{1}".format(url,username))
    print(data.json())
def main():
    startGame()



if __name__ == "__main__":
    while True:
        main()