from lib.blockchain import *
from flask import Flask, request
import requests
import time
import json

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


@app.route("/chain", methods=["GET"])
def get_chain():
    chain_data = []

    for block in chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data), "chain": chain_data})


@app.route("/mine", methods=["GET"])
def mine_transaction():
    # endpoint that mine unfonfirmed transctions
    result = chain.mine()

    if not result:
        return "No Transaction to mine"
    return "Block #{} is mined".format(result)
