from flask import Flask, Response, request, json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET", "POST"])
def home_view():
    if request.method == "GET":
        return "GET is not allowed on this resource."
    return "hi bro"