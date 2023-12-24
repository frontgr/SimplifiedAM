from flask import Flask, request
from flask_cors import CORS
from MongoDB import Database
import Time
import json

app = Flask(__name__)
CORS(app)
MongoClass = Database()


@app.route('/time', methods=['GET'])
def get_time():
    YerevanTime = {'location': 'Yerevan', 'time': ''}
    YerevanTime['time'] = Time.am_time_now()
    LocalToNY = {'data': ''}
    LocalToNY['data'] = Time.user_time_compare()
    outputData = {'Yerevan time': YerevanTime, 'Difference between local and NY times': LocalToNY}
    return json.dumps(outputData)


@app.route('/armenian-cities', methods=['GET'])
def cities():
    return 0


@app.route('/ararat-info', methods=['GET'])
def ararat():
    return 0


@app.route('/armenian-dishes', methods=['GET'])
def dishes():
    return 0


@app.route('/random-armenian-word', methods=['GET'])
def get_rand_word():
    return json.dumps(Database.rand_words())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8086)
