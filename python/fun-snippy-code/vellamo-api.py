from urllib.request import urlopen
import json

url = 'https://vellamo.tampere.fi/api/v1/latest.json'
url_handler = urlopen(url).read().decode()

try:
    js = json.loads(url_handler)
except:
    js = None

lappi = {}

for entry in js:
    name = entry['name']
    if name != 'LAPPI': continue
    for (k,v) in entry.items():
        lappi[k] = v

for (k,v) in lappi['latest_measurements'].items():
    print(k, ':', v)
