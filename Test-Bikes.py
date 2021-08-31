import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "data":
    [
        {
            'day': "0",
            'mnth': "0",
            'year': "0",
            'season': "0",
            'holiday': "0",
            'weekday': "0",
            'workingday': "0",
            'weathersit': "0",
            'temp': "0",
            'atemp': "0",
            'hum': "0",
            'windspeed': "0",
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://77f18616-8000-4caa-b311-0e9a43aa827f.eastus.azurecontainer.io/score'
api_key = 'ftMlcVWMzXHdwhxAu1xW5W3rJhO3zkr3' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))