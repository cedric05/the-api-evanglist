import json
import pathlib
from urllib.parse import parse_qs, urlparse

with open(pathlib.Path(__file__).parent.join('index.json'), 'r') as f:
    api_collections = json.load(f)
apievanglist = []
for collection in api_collections:
    evang = {}
    if '__text' in collection['span']['span']:
        name = collection['span']['span']['__text']
    else:
        name = ''
    collection_id = parse_qs(urlparse(collection['_href']).query)['id'][0]
    evang['name'] = name
    evang['collection_id'] = collection_id
    evang['refer_url'] = collection['_href']
    apievanglist.append(evang)

with open('collections.index.json', 'w') as f:
    json.dump(apievanglist, f)
