from flask import Flask
from flask import request, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ping")
def hello():
    return "pong"

@app.route("/send", methods=['POST'])
def recieve():
    r = requests.post(
        "http://localhost:7070/blocks/phone/in",
        data=json.dumps(request.form)
    )
    print r.text
    return r.text


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
