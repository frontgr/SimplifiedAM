from flask import Flask, request
import requests
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return json.dumps('It is not ready yet!!')


@app.route('/time', methods=['GET'])
def ret_time():
    output = {}
    user_timezone = request.args.get('user_timezone')[3:]
    us_hours = int(user_timezone.split(':')[0])
    usm_minutes = user_timezone.split(':')[1]
    output['difference'] = f"{4 - us_hours}:{usm_minutes}:00"
    return output


@app.route('/armenian-cities', methods=['GET'])
def cities():
    with open('Cities.json') as c:
        return json.load(c)


@app.route('/ararat-info', methods=['GET'])
def get_ararat():
    with open('Ararat.json.json') as a:
        return json.load(a)


@app.route('/armenian-dishes', methods=['GET'])
def dishes():
    with open('Dishes.json') as meal:
        return json.load(meal)


@app.route('/random-armenian-word', methods=['GET'])
def get_rand_word():
    with open('new_dict.json', 'r', encoding='utf-8') as d:
        di = json.load(d)
    ks = list(di.keys())
    url = "https://www.random.org/integers/?num=1&min=0&max=92966&col=5&base=10&format=plain&rnd=new"
    request_number = requests.get(url)
    rand_number = int(request_number.text)
    out = {ks[rand_number]: di[ks[rand_number]]}
    return out


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8086)
