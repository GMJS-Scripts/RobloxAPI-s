from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)


@app.route('/followers/<string:id>', methods=['GET'])
def Get_Followings(id):
    cursor = request.args.get('cursor', default=None)
    username = request.args.get('username', default="(not sended username!)")
    print(id, cursor)

    if cursor:
        FinalLink = f'https://friends.roblox.com/v1/users/{id}/followings?limit=100&&cursor={cursor}&sortOrder=Asc'
    else:
        FinalLink = f'https://friends.roblox.com/v1/users/{id}/followings?limit=100&sortOrder=Asc'
    FinalResult = requests.get(FinalLink)
    FinalResult = FinalResult.json()
    jsonify(FinalResult)
    return FinalResult


app.run(port=5000, host='localhost', debug=True)
