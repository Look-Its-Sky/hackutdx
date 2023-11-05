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
@app.route('/start_server/model/<model>', methods=['GET']):
def start_server(model):
    if process:
        status = "running"

    else:
        status = "starting"
        cmd = ['bash start_linux']
        process = subprocess.Popen(cmd)

    return {
        "result": "success",
        "model": model,
        "status": status
    }

@app.route('/current_model')
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

@app.route('/is_running')
def is_running():
    return {
        "result": "success",
        "running": True if subprocess else False
    }

@app.route('/terminate')
def terminate():
    if process:
        process.terminate()
        return { "result": "success" }
    
    else:
        return { "result": "failure" }
