import os
import datetime
from flask import Flask, Response, jsonify


app = Flask(__name__)

def getenv():
    return "Usama"
    #return os.environ['Name']

@app.route("/")
def replyHello():
    currentDT = datetime.datetime.now()
    result = currentDT.strftime("%Y/%m/%d %H:%M:%S")
    result = result + " Hello " + str(getenv())
    response = jsonify({'result': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)