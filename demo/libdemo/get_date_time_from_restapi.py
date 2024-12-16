import requests

resp = requests.get("https://timeapi.io/api/time/current/zone?timeZone=Asia/Clcutta")

if resp.status_code != 200:
    print("Sorry! Could not get details")
    exit(1)

details = resp.json()  # JSON to dict
print(details['dateTime'])


