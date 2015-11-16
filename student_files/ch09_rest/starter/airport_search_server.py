"""
    airport_search_server.py    -   This is the Flask server to run.  You
                                    will need to run this server and then go to your
                                    browser and browse to localhost:8051

    To get it working properly first however, it requires 3 things to be
    accomplished before it is ready.


    1. Assuming the student_files folder is on your PYTHONPATH, import the
       find_airport() method of the airport.py file.


    Perform steps 2 and 3 as described below.

"""

from flask import Flask, render_template, jsonify, Response
# 1. import find_airport() in airport.py here

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/airport/<code>', methods=['GET'])
def get_airport(code='ord'):
    # 2. call your find_airport method, pass in the code above
    #    using airport_code=code.  Store the return value in a variable.
    try:
        pass
        # 3. remove the pass statement above.
        #    Call jsonify().  Pass into jsonify() the code (code=code)
        #    and also pass the return from find_airport (airport=find_airport_return_value)
        #    set the variable called resp to the return from jsonify()
        #    resp will be your return value for this method (get_airport)
    except KeyError:
        resp = jsonify(airport='Not found. Note: Airport abbreviations are 3 letters codes.')
    
    return Response(resp.data, status=200, mimetype='application/json')

app.run(host='localhost', port=8051)
