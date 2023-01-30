import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


def init_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    return flask_app


app: Flask = init_app()
db: SQLAlchemy = SQLAlchemy(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home() -> str:
    return "Hello World !"
