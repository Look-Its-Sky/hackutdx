from flask import Flask
import os, subprocess
import find_arg

app = Flask(__name__)
process = None

# test route 
@app.route('/', methods=['GET'])
def index():
    return "Hello World!"

# start server if not on
@app.route('/startserver/model/<model>', methods=['GET']):
def start_server(model):
    return {
        "result": "success",
        "model": model
    }

@app.route('/currentmodel')
def current_model():
    args = find_arg("CMD_FLAGS.txt")
    selected_arg = None

    # find model from current arguments
    for arg in args:
        if 'model' in arg:
            selected_arg = arg 

    if selected_arg:
        return {
            "result": "success",
            "model": selected_arg
        }

    return {
        "result": "failure",
        "model": None
    }
