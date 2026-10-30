import os
import requests
try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=24.86&longitude=67.01&current_weather=true"
    weather = requests.get(url, timeout=30).json()["current_weather"]

    payload = {
        "city": "Karachi",
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
    }

    sheet_url = os.environ.get("SHEET_URL")
    if not sheet_url:
        print("ERROR: SHEET_URL environment variable is missing!")
        exit(1)

    response = requests.post(sheet_url, json=payload, timeout=30)
    print("Response status:", response.status_code)
    print("Response text:", response.text)

    if response.text != "OK":
        raise SystemExit("The sheet script said: " + response.text)

except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    exit(1)