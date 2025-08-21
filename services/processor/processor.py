from flask import Flask, request, jsonify

app = Flask(__name__)

def process_header(info):
    # query ip api to get further information

    # return relevant information


    # for now return dummy data
    return {
        "ip": info.get("ip"),
        "country": "Ugunda",
        "user_agent": info.get("user_agent")
    }

@app.route("/process", methods=["POST"])
def process():
    header = request.get_json()
    processed = process_header(header)
    print("Processed:", processed)
    return jsonify({"status": "ok", "data": processed})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
