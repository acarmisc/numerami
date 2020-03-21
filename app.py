# app.py
import os

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route('/save/', methods=['POST'])
def save():
    param = request.form
    print(param)
    return param


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def index(path):
    path_dir = os.path.dirname(os.path.realpath(__file__)) + '/app'
    if path != '' and os.path.exists(os.path.join(path_dir, path)):
        return send_from_directory(os.path.join(path_dir), path)
    else:
        return send_from_directory(os.path.join(path_dir), 'index.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
