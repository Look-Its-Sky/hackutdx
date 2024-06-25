import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    response = flask.jsonify({
        'msg' : 'Hello, World!'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response 

app.run(host='0.0.0.0', port=8000)