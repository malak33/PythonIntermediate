"""

    airport_search_server.py    -   This is the Flask server to run.  You
                                    will need to run this server and then go to your
                                    browser and browse to localhost:8051



"""

from flask import Flask, render_template, jsonify, Response
from ch09_rest.solution.airport import find_airport

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/airport/<code>', methods=['GET'])
def get_airport(code='ord'):
    results = find_airport(airport_code=code)
    try:
        resp = jsonify(airport=results, code=code)
    except KeyError:
        resp = jsonify(airport='Not found. Note: Airport abbreviations are 3 letters codes.')
    
    return Response(resp.data, status=200, mimetype='application/json')

app.run(host='localhost', port=8051)