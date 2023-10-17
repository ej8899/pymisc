# pip3 install requests

import requests 

mac_text = 'dc:a6:32:69:98:98'

url =f'https://www.macvendorlookup.com/api/v2/{mac_text}'

vendor = requests.get(url).json()
vendor_text = vendor[0]['company']

print(vendor_text)