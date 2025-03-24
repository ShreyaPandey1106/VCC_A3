import os
from flask import Flask, render_template, request
import threading
import time

app = Flask(__name__)

cpu_load = False

def generate_load():
    while cpu_load:
        [x**2 for x in range(10000)]  # Generate CPU load

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simulate", methods=["POST"])
def simulate():
    global cpu_load
    action = request.form["action"]
    if action == "start":
        cpu_load = True
        threading.Thread(target=generate_load).start()
    elif action == "stop":
        cpu_load = False
        # Trigger scaling down to 1 instance
        os.system("python3 scale_down.py")
    return render_template("index.html", message="Simulation Updated!")

if __name__ == "__main__":
    app.run(debug=True)