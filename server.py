from flask import Flask, jsonify, request
import subprocess
import threading
import streamlit.web.bootstrap

app = Flask(__name__)

# Start Streamlit app in a separate thread
def start_streamlit():
    subprocess.Popen([r"streamlit", "run", "app.py"])

@app.route("/start-detection", methods=["POST"])
def start_detection():
    """Starts the Streamlit app."""
    threading.Thread(target=start_streamlit).start()
    return jsonify({"message": "Streamlit app started."}), 200

@app.route("/stop-detection", methods=["POST"])
def stop_detection():
    """Stops the Streamlit app."""
    subprocess.Popen(["pkill", "-f", "streamlit"])
    return jsonify({"message": "Streamlit app stopped."}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
