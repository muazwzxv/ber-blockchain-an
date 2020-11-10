from lib.blockchain import *
from flask import Flask, request
import requests
import time
import json

# Setup flask
app = Flask(__name__)

# Setup blockchain Object
chain = Blockchain()

# Setup other host address in the network
peers = set()


@app.route("/node", methods=["POST"])
def register_peer():
    # Host address to peer node
    address = request.get_json()["node_address"]
    if not address:
        return "Invalid data", 400
    # Adds note to peer list
    peers.add(address)

    return get_chain()


# Endpoint to register with an existing node
@app.route("/register_with", methods=["POST"])
def register_with_existing_node():
    """
    Internal endpoint
    -----------------
    Calls the /node endpoint to register current node with the remote node specified
    in the request, and synct the blockchain as well with the remote node
    """
    node = request.get_json()["node_address"]
    if not node:
        return "Invalid data", 400
    data = {"node_address": request.host_url}
    header = {"Content-Type": "application/json"}

    # make request to register with remote node
    response = requests.post(node + "/node", data=json.dumps(data), headers=header)

    if not response.status_code == 200:
        return response.content, response.status_code

    global chain
    global peers

    # update chain and the peers
    chain_dump = response.json()["chain"]
    peers.update(response.json()["peers"])

    return "Registration successful", 200


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


@app.route("/pending", methods=["GET"])
def get_pending_transaction():
    return json.dumps(chain.unconfirmed_transac)


# Helper functions
def create_chain_from_dump(chain_dump):
    chain = Blockchain()

    for i, data in enumerate(chain_dump):
        block = Block(
            data["index"], data["transaction"], data["time"], data["prev_hash"]
        )
        proof = data["hash"]

        if i > 0:
            added = chain.add(block, proof)
            if not added:
                raise Exception("The chain is tempered!!")
        else:
            chain.chain.append(block)

    return chain


def consensus():
    """
    A simple concensus algorithm, if a longer valid chain is found, our
    chain is replaced with it
    """
    global chain

    longest = None
    current = len(chain.chain)

    for node in peers:
        res = requests.get("{}/chain".format(node))
        length = res.json()["length"]
        chain_res = res.json()["chain"]

        if length > current and chain.check_chain_validity(chain_res):
            # Longest new valid chain is found
            current = length
            longest = chain_res

    if longest:
        chain = longest
        return True

    return False
