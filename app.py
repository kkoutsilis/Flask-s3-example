from os import abort
from flask import Flask
from flask import jsonify, request
from flask.typing import ResponseValue
from service import StorageService

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> ResponseValue:
    return jsonify(message="Flask s3 example")


@app.route("/upload", methods=["POST"])
def upload() -> ResponseValue:
    file = request.files.get("file")
    if not file:
        return jsonify(error="File required!"), 400
    storage_service = StorageService()
    res = storage_service.upload("default", file)
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
