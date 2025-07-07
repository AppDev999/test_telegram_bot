import os
from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
    return "Alive"


def run():
    PORT = os.environ.get("PORT")
    app.run(host='0.0.0.0', port=PORT)


def keep_alive():
    t = Thread(target=run)
    t.start()
