#Calling Google GeoJSON API
#Don't forget to enter your Google Api Key below
#import libs
import urllib.request , urllib.parse , urllib.error
import json
import ssl

#Ignore ssl
cer = ssl.create_default_context()
cer.check_hostname = False
cer.verify_mode = ssl.CERT_NONE

#Ask for an address from user
address = input("Enter-")

#Quit if there is no input
if len(address) < 1:
    quit()

#Enter your Goggle API KEY
api_key = 42
url_name = "https://maps.googleapis.com/maps/api/geocode/json?"

#Encode address and api_key to url
tem_address = dict()
tem_address['address'] = address
tem_address['key'] = api_key
url = url_name + urllib.parse.urlencode(tem_address)

#Open url
print("Retrieving:",url_name)
fhand = urllib.request.urlopen(url , context = cer)
#Decode data from url
data = fhand.read().decode()
print("Retrieved:",len(data),"characters")

#Create json obj. if possible
try:
    data_js = json.loads(data)
except:
    data_js = None

#Print result for debugging
print(json.dumps(data_js,indent = 4))

#Check status and quit if not OK
if not data_js or 'status' not in data_js or data_js['status'] != 'OK':
    print('=== Failure ====')
    quit()

#Print place_id (the value I am interested in now)
print(data_js['results'][0]['place_id'])
