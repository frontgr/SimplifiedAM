from flask import Flask
from flask_cors import CORS
from MongoDB import Database
import Time
import json
from Sqlite3DB import SQLDB


app = Flask(__name__)
CORS(app)

database = Database()


@app.route('/', methods=['GET'])
def index():
    return json.dumps('It is not ready yet!!')


@app.route('/get-time', methods=['GET', 'POST'])
def return_time():
    output = {'location': 'Yerevan'}
    output['time'] = Time.am_time_now()
    # Try request
    return output


@app.route('/armenian-cities', methods=['GET'])
def cities():
    return 0


@app.route('/ararat-info', methods=['GET'])
def get_ararat():
    db = SQLDB()
    if db.output_ararat():
        return {'status': 'Ok', 'output': db.output_ararat()}
    else:
        return {'message': 'error', 'message': 'Oops, something went wrong!'}


@app.route('/armenian-dishes', methods=['GET'])
def dishes():
    return 0

#
# @app.route('/random-armenian-word', methods=['GET'])
# def get_rand_word():
#     return json.dumps(json_util.dumps(database.rand_words()), ensure_ascii=False).encode('utf8')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8086)
