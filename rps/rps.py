import random, requests, json, pandas as pd



def getInput():
    noCorrectAnswer = True
    while (noCorrectAnswer):
        noCorrectAnswer = False
        inputP = input("Choose between: 0/rock, 1/spock, 2/paper, 3/lizzard, 4/scissors, 5/exit:    ")
        playerInput = -1

        if (inputP.isdigit()):
            if int(inputP) in [0,1,2,3,4,5]:
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
                    print("not a availabe choice\n")

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


def playARound(currentPlayer,difficulty,currentGame = [0,0]):
    playerChoice = getInput()
    if playerChoice == 5:
        print("Results:")
        print("Games played:\t", len(currentGame) - 2)
        print("Games won:\t", currentGame[0])
        print("Games drawn:\t", currentGame[1])
        startGame()


    if playerChoice != 5:
        if difficulty== 0:
            compChoice = random.randrange(0,4)
        else:
            if len(currentGame)-2 < 5:
                compChoice = random.randrange(0, 4)
            else:
                lastGames = currentGame[-5:]
                goingToPlay = max(set(lastGames), key=lastGames.count)
                compChoice = (goingToPlay+1)%5


        print("You chose: "+toName(playerChoice)+"\tComputer chose: "+toName(compChoice))

        result = checkResult(playerChoice, compChoice)
        if result == "player won":
            currentGame[0]+=1
        elif result == "draw":
            currentGame[1]+=1

        print(result+"\n")

        print(currentPlayer,toName(playerChoice))

        sendData(currentPlayer,toName(playerChoice))

        currentGame.append(playerChoice)

        playARound(currentPlayer,difficulty,currentGame)


def startGame():
    inputP = input("\nChoose between (1/playNormal),(2/playHard), (3/data), (4/userData) or (5/exit):  \n")

    if inputP.isdigit() and int(inputP) in [1,2,3,4,5]:
        inputP = int(inputP)
        match inputP:
            case 1:
                currentPlayer = input("playerName:  ").strip()
                if currentPlayer == None or currentPlayer=="":
                    print("not valid")
                    startGame()
                else:
                    playARound(currentPlayer,0,[0,0])
            case 2:
                currentPlayer = input("playerName:  ").strip()
                if currentPlayer == None or currentPlayer == "":
                    print("not valid")
                    startGame()
                else:
                    playARound(currentPlayer, 1, [0, 0])
            case 3:
                getData()
            case 4:
                inputP = input("Which user?")
                getUserData(inputP.strip())
            case 5:
                exit()
            case other:
                print("something went wrong!")


def sendData(playerName,symbol, url="http://127.0.0.1:5000"):
    data = {"Name":playerName,"Symbol": symbol,"Symbolanzahl":1}

    requests.put(url, json.dumps(data))

def getData(url="http://127.0.0.1:5000/getData"):
    data = requests.get(url)
    if data == None:
        print("Something went wrong")
        return

    data = data.json()
    print("Total games played: \t",data["totalPlays"],"\n")
    choicesData = data["choicesCount"]
    highestData = data["mostChoosen"]
    print("Choices occurrences:")
    for i in choicesData:
        print("\t",i,": \t",choicesData[i])
    print("\nHighest choices:")
    for i in highestData:
        print("\t",i,": \t",highestData[i])

def getUserData(username, url="http://127.0.0.1:5000"):
    data = requests.get("{0}/{1}".format(url,username))
    print(json.dumps(data.json()))
def main():
    startGame()



if __name__ == "__main__":
    while True:
        main()