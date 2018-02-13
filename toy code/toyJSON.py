import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"  #3
payload = {"longUrl": "http://example.com"} #1
headers = {"Content-Type": "application/json"}  #4
r = requests.post(url, json=payload)       #2

# print(r.text)
# print(json.loads(r.text))
print(json.loads(r.text)["error"]["code"])

print(r.headers)