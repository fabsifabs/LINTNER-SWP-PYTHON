from flask import Flask, request, jsonify, render_template
from os.path import exists
import pandas as pd
import json
app = Flask(__name__)


@app.route('/')
def index():
    print("rendering")
    print(type(getAllData()))
    return render_template("index.html", data = getAllData())

@app.route('/', methods=['PUT'])
def addUserData():
    m = json.loads(request.data)
    data = getAllData()
    print(m["Name"],m["Symbol"],m["Symbolanzahl"])
    if m["Name"] in data:
        if m["Symbol"] in data[m["Name"]]:
            data[m["Name"]][m["Symbol"]]+=int(m["Symbolanzahl"])
        else:
            data[m["Name"]][m["Symbol"]]=int(m["Symbolanzahl"])

        updateData(data)
        return "Success"
    else:
        data[m["Name"]]={m["Symbol"] : m["Symbolanzahl"]}
        updateData(data)
        return "Success"

    print("Failure")
    return "Failure"

@app.route('/getData', methods=['GET'])
def getData():
    data = getAnalysedData()
    return json.dumps(data)

@app.route('/<username>',methods=['GET'])
def getUserData(username):
    print("Sending userdata")
    data = getAllData()
    if username in data:
        return json.dumps(data[username])
    else:
        return {"Error":"No User found"}

def getAnalysedData(path = "data.json"):
    print("Sending Data")
    if not exists(path):
        f = open("data.json", "x")
        return {}
    else:
        with open(path) as d:
            data = json.load(d)
            if data == None:
                return {}

        data = analyseData(data)
        print(data)
        print("success")
        return data

def getAllData(path = "data.json"):
    if not exists(path):
        f = open("data.json", "x")
        return {}
    else:
        with open(path) as d:
            data = json.load(d)
            if data == None:
                return {}
    return data
def deleteUserData(username,path = "data.json"):
    data = getAnalysedData(path)
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
    app.run(debug=True,threaded=True)