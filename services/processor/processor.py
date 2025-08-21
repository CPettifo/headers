from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def process_header(info):
    ip = info.get("ip")
    user_agent = info.get("user_agent")
    try:
        ip_info_response = requests.get(f"https://ipinfo.io/{ip}/json")
        ip_info = ip_info_response.json()
    except Exception as e:
        ip_info = {"error": str(e)}

    return {
        "ip": ip,
        "user_agent": user_agent,
        "ip_info": ip_info
    }

@app.route("/process", methods=["POST"])
def process():
    header = request.get_json()
    processed = process_header(header)
    return jsonify({"status": "ok", "data": processed})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
