import sys          # to handle argument values
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : 'U5GE7wPNox8JkvtuXPiroo5fJDuGuYa9',
                    'Content-Type' : 'application/json' }
host = 'localhost'

if(len(sys.argv) != 4): # If the module, channel, and/or value are not provided.
        print 'Please provide module #, channel #, and value [1|0].'
        print 'Exiting script . . .'
        exit() # Inform the user and exit the script.

mod = sys.argv[1] # 1st argument = module number
chn = sys.argv[2] # 2nd argument = channel number
# 3rd argument = convert value to be written from 1/0 to true/false
val = 'true' if(sys.argv[3] == '1') else 'false'
# construct request URL for the 'local' built-in rack of I/O *state*
url = 'https://'+host+'/manage/api/v1/io/local/modules/'+mod+'/channels/'+chn+'/digital/state'
# data is a JSON object that formats the value for the request
payload = '{"value":' + val + '}';
print('Writing ' + payload + ' to output ' + chn + ' on module ' + mod)
# make the RESTful put request and save the response
response = requests.put(url, data=payload, headers=head, verify=False)
# use the response code to determine if the write worked or not
if response.status_code == 200: print('Write success!')
else: print('Write request failed.')
