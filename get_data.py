import requests

client_id = '07a7c3bb-8669-4253-ac39-c6fb21908dcc'

endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': 'SN18700,SN90450',
    'elements': 'mean(air_temperature P1D)',
    'referencetime': '1990-04-01/2018-04-03',
}

r = requests.get(endpoint, parameters, auth=(client_id,''))
json = r.json()
print(r)
#print(json)
