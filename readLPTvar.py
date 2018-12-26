from apiKey import key
import sys          # to handle argument values
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : key,
            'Content-Type' : 'application/json' }
host = 'localhost'

# construct request URL to read the Pressure_Transducer_1 float:
url = 'https://'+host+'/pac/device/strategy/vars/floats/Pressure_Transducer_1'
# make the RESTful get request and save the response
response = requests.get(url, headers=head, verify=False)
# if the request failed, alert the user and exit the script
if response.status_code != 200:
    print('Read request failed.')
    sys.exit()
# otherwise find the state result in the response text, then output it
else:
    start = response.text.index('value') + 7
    end = response.text.index('}', start) - 2
    val = float(response.text[start:end]) * 10
    print(str(val))
