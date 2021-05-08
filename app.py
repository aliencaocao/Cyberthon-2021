import os
import json
from flask import Flask, request

app = Flask(__name__)

votes = {
    "pwn": 0,
    "web": 0,
    "crypto": 0,
    "forensics": 0,
    "rev": 0,
    "misc": 0
}

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/votes')
def get_votes():
    return json.dumps(votes)

@app.route('/vote')
def vote():
    choice = request.args.get("choice")
    votes[choice] += 1
    return json.dumps(votes)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
