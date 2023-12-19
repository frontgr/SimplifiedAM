from flask import Flask, request
import json
from flask_cors import CORS
from MongoDB import Database


app = Flask(__name__)
CORS(app)
MongoClass = Database()


@app.route('/', methods=['GET'])
def test():
    return MongoClass.TestDB()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8086)
