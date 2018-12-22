from apiKey import Manage_key
import sys          # to handle argument values
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : Manage_key,
                    'Content-Type' : 'application/json' }
host = 'localhost'

if(len(sys.argv) != 2): # If the value is not provided.
        print 'Please specify "on" or "off".'
        print 'Exiting script . . .'
        exit() # Inform the user and exit the script.

# 1st argument = convert value to be written from on/off to true/false
val = 'true' if(sys.argv[1] == 'on') else 'false'
# construct request URL for the 'local' built-in rack of I/O *state*
url = 'https://'+host+'/manage/api/v1/io/local/modules/0/channels/22/digital/state'
# data is a JSON object that formats the value for the request
payload = '{"value":' + val + '}';
print('Writing ' + payload + ' to Python_Output at channel 22')
# make the RESTful put request and save the response
response = requests.put(url, data=payload, headers=head, verify=False)
# use the response code to determine if the write worked or not
if response.status_code == 200: print('Write success!')
else: print('Write request failed.')
