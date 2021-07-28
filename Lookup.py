import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from json import load
import socket
import errno

#https://geolocation-db.com/json/39.110.142.79&position=true
#http://ipinfo.io/8.8.8.8/json
#use this to look up an ip
#build ip cache checker, to see if we already have it on file?

def IPGeo(IP):

    #url = 'http://ip-api.com/json/' + IP.strip()
    #url = 'http://api.ipgeolocationapi.com/geolocate/' + IP.strip()
    #print("url is: ", IP.strip())
    url = 'https://api.ipregistry.co/' + IP.strip() + '?key=jze32dn4runof747'
    try:
        result = urlopen(url)
        data = load(result)
    except HTTPError as err:
        #print("Error!")
        #print(err.code)
        data = {"ip" : IP.strip(), "type" : "Multicast"}
      
    return data

def RDAP(IP):
    #rdap look up thing
    url = 'https://rdap.arin.net/registry/ip/' + IP.strip()
    try:
        result = urlopen(url)
        data = load(result)

    except HTTPError as err:
        print("Error!")
        print(err.code)
        data = {"ip": IP.strip(), 'RDAP': "unknown"}

    data = IP.strip()+ ":" + str(data)
    return data

