from apiKey import Manage_key
import time         # to sleep
import requests     # to make get/post requests
# ignore insecure https requests warning:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# head is a JSON object that holds API key information
head = {    'apiKey' : Manage_key,
                    'Content-Type' : 'application/json' }
host = 'localhost'
val = 'true'
# construct request URL for the 'local' built-in rack of I/O *state*
url = 'https://'+host+'/manage/api/v1/io/local/modules/0/channels/22/digital/state'

for x in range(45):
    val = 'false' if val == 'true' else 'true'
    payload = '{"value":' + val + '}'
    response = requests.put(url, data=payload, headers=head, verify=False)
    time.sleep(0.333)
