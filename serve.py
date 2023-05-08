from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

seed = int(0)

@app.route('/', methods=['GET'])
def query_ip():
    return socket.gethostname()


@app.route('/', methods=['POST'])
def launch_ec2():
    return subprocess.Popen("/home/ec2-user/CCAMP2/stress_cpu.py")

if (__name__ == "__main__"):
    app.run(debug=True, host="0.0.0.0", port=8080)