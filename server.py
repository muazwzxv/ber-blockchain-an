from lib.blockchain import *
from flask import Flask, request
import requests
import time

# Setup flask
app = Flask(__name__)

# Setup blockchain Object
chain = Blockchain()
print(chain)


@app.route("/tranaction", methods=["POST"])
def new_transaction():
    data = request.get_json()
    fields = ["author", "content"]

    for field in fields:
        if not data.get(field):
            return "Invalid Transaction data", 404
    
    data["time"] = time.time()
    chain.add(data)

    return "Success", 201