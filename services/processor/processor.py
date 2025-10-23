from flask import Flask, request, jsonify
from datetime import date
import requests, pycountry, logging
from dotenv import load_dotenv, dotenv_values

# This service will process the header from the collector service, storing non-personal
# data in the database, and returning all data to the browser session
# A call is made to ipinfo.io to get more information about the visitor's ip address

load_dotenv()


app = Flask(__name__)

def process_header(info):
    ip = info.get("ip")
    user_agent = info.get("user_agent")
    try:
        url = f"https://vpnapi.io/api/{ip}?key={os.getenv('VPNAPI_key')}"
        print(f"DEBUG: Requesting URL: {url}", flush=True) 
        
        ip_response = requests.get(url)
        print(f"DEBUG: HTTP status code: {ip_response.status_code}", flush=True)

        ip_info = ip_response.json()
        print(f"DEBUG: Received ip_info: {ip_info}", flush=True)
        
    except Exception as e:
        print(f"DEBUG: Exception during API call: {e}", flush=True)
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
    # INSERT INTO logs (date, country, user_agent)
    # VALUES (values.date, values.country, values.user_agent)


    return 0


@app.route("/process", methods=["POST"])
def process():
    header = request.get_json()
    response = process_header(header)

    location_info = response["ip_info"].get("location")
    if not location_info:
        country = "AU"
    else:
        country = location_info["country"]


    # separate values to store
    values = {
        "country": country,
        "user_agent": response["user_agent"]
    }

    write_to_db(values)
    return jsonify({"status": "ok", "data": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
