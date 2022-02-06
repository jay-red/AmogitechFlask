from flask import Flask, Response, request, json
from flask_cors import CORS

from werkzeug.utils import secure_filename

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["GET", "POST"])
def home_view():
    if request.method == "GET":
        return "GET is not allowed on this resource."

    if "amogi-file" not in request.files:
        return "amogi-file is required."

    amogi_file = request.files["amogi-file"]

    if ( not amogi_file ) or amogi_file.filename == "":
        return "amogi-file is required."

    amogi_file.save( secure_filename( amogi_file.filename ) )

    return "hi bro"