import os
import datetime
import argparse
from flask import Flask, Response, jsonify


app = Flask(__name__)

def getenv():
    return os.environ['NAME']

@app.route("/")
def replyHello():
    currentDT = datetime.datetime.now()
    result = currentDT.strftime("%Y/%m/%d %H:%M:%S")
    result = result + " Hello " + str(getenv())
    response = jsonify({'result': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Start Flask Server')

    parser.add_argument("-ip", default="0.0.0.0", help='IP to start server on')
    parser.add_argument("-port", default=8080, help='sum the integers (default: find the max)')
    args = parser.parse_args()

    app.run(args.ip, port=args.port, debug=True)
