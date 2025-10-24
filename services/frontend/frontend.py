from flask import Flask, request, render_template
import requests, pycountry

# This service will collect the information from the user and send it to the processor to return
# information about the visitor based on their IP address.

# It also stores the templates for the index and analytics pages.

# TODO: Rename app to something more appropriate as it will also serve the Flask templates


app = Flask(__name__)
processor_url = "http://collector:5000/process"

@app.route("/", methods=["GET"])


@app.route("/send", methods=["GET"])
def send_headers():
    headers = dict(request.headers)
    public_headers = {"ip": headers.get("Cf-Connecting-Ip"),
                      "user_agent": headers.get("User-Agent")}
    try:
        response = requests.post(processor_url, json=public_headers)
        data = response.json()
        ip_info = data.get("data", {}).get("ip_info", {})

        agent = headers.get("User-Agent")
        security_info = ip_info.get("security")
        location_info = ip_info.get("location")
        country_info = pycountry.countries.get(alpha_2=location_info["country_code"])
        country = country_info.name
        flag = country_info.flag
        region = location_info.get("region")
        city = location_info.get("city")
        vpn = security_info.get("vpn")
        proxy = security_info.get("proxy")
        tor = security_info.get("tor")
        relay = security_info.get("relay")
        

        return render_template("index.html", 
                               agent=agent, 
                               # test hardcoding something here
                               country=country, 
                               country_flag=flag,
                               city=city, 
                               region=region,
                               vpn=vpn,
                               proxy=proxy,
                               tor=tor,
                               relay=relay,                               
                               # test getting the request.headers instead of having it as a dict
                               user_headers=request.headers)


    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)