import requests
import time

processor_url = "http://processor:5000/process"

def main():
    headers = collect_headers()
    try:
        response = requests.post(processor_url, json=headers)
        print("sent headers, response from processor:", response.status_code)
        print("Response json: ", response.json())
    except Exception as e:
        print("Error: ", e)

def collect_headers():
    # for now just return wikipedia's ip
    return {
        "ip": "208.80.154.224",
        "user_agent": "Mozilla/5.0"
    }



if __name__ == "__main__":
    main()