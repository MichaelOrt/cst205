import requests, json
from pprint import pprint

my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
    'api_key': my_key,
    'start_date': '2017-03-09',
    'end_date': '2017-03-11'
}

endpoint = 'https://api.nasa.gov/planetary/apod'

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    pprint(data)
except:
    print('please try again')