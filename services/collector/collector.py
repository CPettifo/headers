from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
processor_url = "http://processor:5000/process"

@app.route("/")
def home_route():
    return {"message": "Collector is running"}


@app.route("/send", methods=["GET"])
def send_headers():
    headers = collect_headers()
    try:
        response = requests.post(processor_url, json=headers)
        return {
            "sent_headers": headers,
            "processor_status": response.status_code,
            "processor_response": response.json()
        }
    except Exception as e:
        return {"error": str(e)}, 500

def collect_headers():
    # for now just return wikipedia's ip
    return {
        "ip": "208.80.154.224",
        "user_agent": "Mozilla/5.0"
    }

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)