from flask import Flask, jsonify, request
import requests, datetime

app = Flask(__name__)
processor_url = "http://processor:5000/process"

@app.route("/")
def home_route():
    return {"message": "Collector is running"}


@app.route("/send", methods=["GET"])
def send_headers():
    headers = dict(request.headers)
    public_headers = {"ip": request.remote_addr,
                      "user_agent": headers.get("User-Agent")}
    try:
        response = requests.post(processor_url, json=public_headers)
        data = response.json()
        return {
            # should convert this from country code to country name
            "country": data.get("country"),
            "time": datetime.datetime.now(),
            "isp": data.get("org"),
            "full_response": response.json(),
            "processor_status": response.status_code,
            "sent_headers": public_headers
        }
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)