from flask import Flask, request, jsonify
from os.path import exists
import pandas as pd
import json
app = Flask(__name__)


@app.route('/')
def index():
    data = getData()
    return data

@app.route('/', methods=['PUT'])
def addUserData():
    m = json.loads(request.data)
    data = getData()
    print(m["Name"],m["Symbol"],m["Symbolanzahl"])
    if m["Name"] in data:
        if m["Symbol"] in data[m["Name"]]:
            data[m["Name"]][m["Symbol"]]+=m["Symbolanzahl"]
            print(1)
        else:
            print(2)
            data[m["Name"]][m["Symbol"]]=m["Symbolanzahl"]

        updateData(data)
        return "Success"
    else:
        print(3)
        data[m["Name"]]={m["Symbol"] : m["Symbolanzahl"]}
        updateData(data)
        return "Success"

    print("Failure")
    return "Failure"

@app.route('/', methods=['GET'])
def getData():
    return json.dumps(getData)

@app.route('/<username>',methods=['GET'])
def getUserData(username):
    data = getData()
    print(data)
    print(data[username])
    return json.dumps(data[username])

def getData(path = "data.json"):
    if not exists(path):
        f = open("data.json", "x")
        return {}
    else:
        with open(path) as d:
            data = json.load(d)
            if data == None:
                return {}

        data = analyseData(data)
        print(type(data))
        print(data)
        return json.dumps(data)

def deleteUserData(username,path = "data.json"):
    data = getData(path)
    if username in data:
        del data[username]
        updateData(data)
    else:
        return

def updateData(data,path = "data.json"):
    with open(path, 'w') as d:
        json.dump(data, d)


def analyseData(data):
    df = pd.DataFrame(data)
    df  = df.fillna(0).astype(int)
    totalPlays = df.sum().sum()
    choicesCount = df.sum(axis = 1).to_frame().astype("int32")
    mostChoosen = choicesCount.max()
    mostChoosen=mostChoosen.values
    mostChoosen = choicesCount.loc[choicesCount[0]==mostChoosen[0]]
    mostChoosen= mostChoosen.to_dict()
    mostChoosen = mostChoosen[0]
    choicesCount = choicesCount.to_dict()
    choicesCount = choicesCount[0]
    return {"totalPlays": int(totalPlays),"choicesCount":choicesCount,"mostChoosen":mostChoosen}


if __name__ == '__main__':
    app.run()