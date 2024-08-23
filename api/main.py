import flask, os

DEBUG = os.getenv('DEBUG')
app = flask.Flask(__name__)

@app.route('/')
def index():
    response = flask.jsonify({
        'msg' : 'Hello, World!'
    })

    return response 

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Credentials', 'true')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=DEBUG)

