from flask import Flask, render_template
from flask import request, jsonify, redirect

app = Flask(__name__,static_url_path='')

@app.route('/getFrames', methods=['GET'])
def getFrames():
    return "Hello"

app.run(host="localhost",port=54321,threaded=True)