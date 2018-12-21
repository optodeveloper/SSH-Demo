import sys          # to handle argument values
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : 'U5GE7wPNox8JkvtuXPiroo5fJDuGuYa9',
            'Content-Type' : 'application/json' }
host = 'localhost'

if(len(sys.argv) != 3): # If the module and/or channel are not provided.
    print 'Please provide module # and channel #.'
    print 'Exiting script . . .'
    exit() # Inform the user and exit the script.

mod = sys.argv[1] # 1st argument = module number
chn = sys.argv[2] # 2nd argument = channel number
# construct request URL for the 'local' built-in rack of I/O *status*
url = 'https://'+host+'/manage/api/v1/io/local/modules/'+mod+'/channels/'+chn+'/digital/status'
# make the RESTful get request and save the response
response = requests.get(url, headers=head, verify=False)
# if the request failed, alert the user and exit the script
if response.status_code != 200:
    print('Read request failed.')
    sys.exit()
# otherwise find the state result in the response text, then output it
else:
    start = response.text.index('state') + 7
    end = response.text.index(',', start)
    print(response.text[start:end])
