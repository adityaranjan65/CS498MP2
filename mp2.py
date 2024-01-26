from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Create a separate process for running stress_cpu.py
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return {"message": "CPU stress initiated successfully"}

@app.route('/', methods=['GET'])
def get_private_ip():
    # Get the private IP address using socket
    private_ip = socket.gethostbyname(socket.gethostname())
    return {"private_ip": private_ip}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4999)