from flask import Flask, jsonify
 
app = Flask(__name__)
 

@app.route("/health", methods=["GET"])
def get_health():
    return jsonify({'health': 'OK'})


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({'status': 'OK'})