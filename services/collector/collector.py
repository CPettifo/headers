from flask import Flask, request, render_template
import requests, pycountry

# This service will collect the information from the user and send it to the processor to return
# information about the visitor based on their IP address.

# It also stores the templates for the index and analytics pages.

# TODO: Rename app to something more appropriate as it will also serve the Flask templates


app = Flask(__name__)
processor_url = "http://processor:5000/process"

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
        country_info = pycountry.countries.get(alpha_2=ip_info["country"])
        country = country_info.name
        flag = country_info.flag
        city = ip_info.get("city")
        full_response = data
        full_code_response = response.status_code
        

        return render_template("index.html", 
                               agent=agent, 
                               # test hardcoding something here
                               country=country, 
                               country_flag=flag,
                               city=city, 
                               # test getting the request.headers instead of having it as a dict
                               user_headers=request.headers)


    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)