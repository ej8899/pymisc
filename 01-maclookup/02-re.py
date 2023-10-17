import subprocess
import requests
import re
from time import sleep

command = 'arp -a'
response = subprocess.check_output(command, shell=True)
#print (response)
#exit(1)

response = str(response).split('\\n')
#print (f'response:{response}')
#exit(1)
for line in response:
    #print(f'working on: {line}');
    ip_text = ''
    mac_text = ''
    vendor_text = ''

    try:
          ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
          #print(f'IP:{ip["match"]}')
          if ip_match:
              ip_text = ip_match.group(0)
              ip_text = ip_text.replace('(','')
              ip_text = ip_text.replace(')','')
              #print(f"found IP: {ip_text}")
          else:
              print(f"no IP found in {line}")
    except:
          pass
    
    try:
          mac = re.search(r'([0-9A-Fa-f]{1,2}[:-]){5}[0-9A-Fa-f]{1,2}',line)
          mac_text = mac.group()
          if mac:
              formatted_mac = mac.group(0).replace(":", "-")
              #print("Found MAC address:", formatted_mac)
          else:
              print("No MAC address found")
          #print(f'fetching on IP:{ip_text}, MAC:{formatted_mac}')
          #url = f'https://www.macvendorlookup.com/api/v2/{mac_text}'
          url = f'https://api.macvendors.com/{formatted_mac}'
          try:
                request = requests.get(url)
                print(f"RESPONSE:{request}")
                if request.status_code == 200:
                    vendor_text = request.text
                    #print(f"VENDOR:{vendor}")
                else:
                    vendor_text = "Not found."
          except:
                pass
    except:
          pass
    print(f'Record:\t{ip_text}\t{mac_text}\t{vendor_text}\n')
    sleep(1)