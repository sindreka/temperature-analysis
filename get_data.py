import requests

client_id = '07a7c3bb-8669-4253-ac39-c6fb21908dcc'

name = "oslo"
endpoint = 'https://frost.met.no/sources/v0.jsonld'
parameters = {
    "name" : f'*{name}*',
}
r = requests.get(endpoint,parameters, auth=(client_id,''))
d = r.json()

sensor = d["data"][0]["id"]



# burde kunne velge tidsperiode?

endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources': sensor,
    'elements': 'mean(air_temperature P1M)',
    'referencetime': '1990-04-01/1991-04-03',
}

r = requests.get(endpoint, parameters, auth=(client_id,''))
data = r.json()["data"]

for d in data:
    print(f'{d["referenceTime"].split("T")[0][:-3]} : {d["observations"][0]["value"]} {d["observations"][0]["unit"]} ' )

with open("data.txt","w") as file:
    file.write(f"date,temperature\n")
    for d in data:
        file.write(f"{d['referenceTime'].split('T')[0][:-3]},{d['observations'][0]['value']}\n")




