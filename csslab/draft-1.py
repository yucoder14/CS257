import sys
import flask
from flask import render_template as render, request

# Live reload: flask --app draft-1.py --debug run --port 5115

app = flask.Flask(__name__, '/static', template_folder='templates')

# Index
@app.route("/")
def index():
    return render('index.html')


if __name__ == "__main__":
    port = 5132
    app.run(host="0.0.0.0", port=port, debug=True)
