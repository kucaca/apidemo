from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

RESPONSE_SUCCESS = 0
RESPONSE_ERROR = 1

def CResponse(code, data, msg = ''):
    response = {
        "code": code,
        "data": data,
        "msg": msg
    }
    return json.dumps(response), 200, { 'Content-Type': 'application/json'}

@app.route('/pagelist')
def PageList():
    data = [
            {"name": "张三", "age": 14, "sex": 0},
            {"name": "王四", "age": 19, "sex": 1},
        ]
    return CResponse(RESPONSE_SUCCESS, data)

if __name__ == '__main__':
    app.run()