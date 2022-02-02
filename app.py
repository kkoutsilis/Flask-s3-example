from flask import Flask, jsonify
from flask.typing import ResponseValue

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> ResponseValue:
    return jsonify(message="Flask s3 example")
