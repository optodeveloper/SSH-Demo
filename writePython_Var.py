import sys          # to handle argument values
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : 'mffmCamugXoBoj7jq4zRzCG8ksNtv8gg',
                    'Content-Type' : 'application/json' }
host = 'localhost'

if(len(sys.argv) != 2): # If the value is not provided.
        print 'Please provide integer value.'
        print 'Exiting script . . .'
        exit() # Inform the user and exit the script.

val = sys.argv[1] # 1st arguement = value to write
# construct request URL for the strategy "Python_Var" int32
url = 'https://'+host+'/pac/device/strategy/vars/int32s/Python_Var'
# data is a JSON object that wraps the value for the request
payload = '{"value":' + val + '}';
print('Writing ' + payload + ' to Python_Var')
# make the RESTful put request and save the response
response = requests.post(url, data=payload, headers=head, verify=False)
# use the response code to determine if the write worked or not
if response.status_code == 200: print('Write success!')
else: print('Write request failed.')
