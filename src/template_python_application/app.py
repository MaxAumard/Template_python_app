from flask import Flask


def init_app():
    return Flask(__name__)


app = init_app()


@app.route("/")
def home():
    return "Hello World !"
