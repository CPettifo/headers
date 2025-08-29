from flask import Flask, request, jsonify
from datetime import date
import requests, pycountry

app = Flask(__name__)

def process_header(info):
    ip = info.get("ip")
    user_agent = info.get("user_agent")
    try:
        ip_info_response = requests.get(f"https://ipinfo.io/{ip}/json")
        ip_info = ip_info_response.json()

        if "country" in ip_info:
            country = pycountry.countries.get(alpha_2=ip_info["country"])
            ip_info["country_name"] = country.name if country else ip_info["country"]

    except Exception as e:
        ip_info = {"error": str(e)}

    return {
        "ip": ip,
        "user_agent": user_agent,
        "ip_info": ip_info
    }

def write_to_db(values):
    # get today's date
    date_today = date.today().isoformat()

    # connect to db
    
    # write to db
    # INSERT INTO logs (date, country)
    # VALUES (values.date, values.country)


    return 0


@app.route("/process", methods=["POST"])
def process():
    header = request.get_json()
    response = process_header(header)
    # separate values to store
    values = {
        "country": response["ip_info"].get("country_name"),
        "user_agent": response["user_agent"]
    }

    write_to_db(values)
    return jsonify({"status": "ok", "data": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
