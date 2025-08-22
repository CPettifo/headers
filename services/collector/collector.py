from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
processor_url = "http://processor:5000/process"

@app.route("/")
def home_route():
    return {"message": "Collector is running"}


@app.route("/send", methods=["GET"])
def send_headers():
    headers = dict(request.headers)
    # get the connecting IP from the Cloudflare tunnel
    ip = request.headers.get("CF-Connecting-IP", request.remote_addr)
    # For now replace this with geeks for geeks ip
    # ip = "13.248.169.48"
    public_headers = {"ip": ip,
                      "user_agent": headers.get("User-Agent")}
    try:
        response = requests.post(processor_url, json=public_headers)
        return {
            "sent_headers": public_headers,
            "processor_status": response.status_code,
            "processor_response": response.json()
        }
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)