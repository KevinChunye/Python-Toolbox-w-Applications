import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

response.raise_for_status()

# the json file is in a dictionary formate, then you can call with square bracket for specific element
latitude = response.json()['iss_position']['latitude']
longitude = response.json()['iss_position']['longitude']

iss_position = (latitude,longitude)

print(iss_position)

"""
different responses:
1XX Hold on
2XX Here you go
3XX go away
4XX you screwed up, the user is lost
5XX I screwed up, the server is down


if response.status_code != 200:
    raise Exception("Bad response from ISS API")
    
    
#https://www.webfx.com/web-development/glossary/http-status-codes/
#staus code dictionary
if response.status_code == 404:
    raise Exception("The resource is not exist")
elif response.status_code == 401:
    raise Exception("you are not authorized to open")
"""

