import requests
import json

print('Requesting...')
url = 'https://platform.antares.id:8443/~/antares-cse/antares-id/{}/{}'.format('weather-station', 'station1')

headers = {
    'X-M2M-Origin' : 'b4e89ce2436b9d90:202c7b14b849c084',
    'Content-Type' : 'application/json;ty=4',
    'Accept' : 'application/json',
}
data = 'helo'
strData = ''
try:
    strData = json.dumps(data)    
except:
    strData = data

dataTemplate = {
    "m2m:cin" : {
        "con" : "hullo",
    }
}
dataTemplate = json.dumps(dataTemplate)

print(dataTemplate)
print(url)

r = requests.post(url, headers=headers, data=dataTemplate)
response = r.text
print(response)
# return response
