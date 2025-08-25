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
    public_headers = {"ip": headers.get("Cf-Connecting-Ip"),
                      "user_agent": headers.get("User-Agent")}
    try:
        response = requests.post(processor_url, json=public_headers)
        return {
            "country": response.country,
            "city": response.city,
            "full_response": response.json(),
            "full_code_response": response.status_code,
            "sent_headers": public_headers,
            "user_headers": headers,
            "current_time": datetime.datetime.now()
        }
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)