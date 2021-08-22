import argparse
import json
import os
import pathlib
import sys
import requests


package_dir = pathlib.Path(__file__).parent
parser = argparse.ArgumentParser(
    description='Import collections from workspace')
parser.add_argument('--workspace_id',
                    default="411ed77a-1f63-4df2-acf4-9bb0da7a3aab",
                    help='workspace_id for postman import')
parser.add_argument('--baseurl',
                    default="https://www.postman.com/api-evangelist/workspace/amazon-web-services-aws",
                    help='base_url to visit postman collection')

parser.add_argument('--postmanapikeys',
                    default=str(package_dir.joinpath(
                        '.postmanapikeys.json')),
                    help='postmanapikeys to retrieve information from postman')
parser.add_argument('--index',
                    default=str(package_dir.joinpath('collections.index.json')),)

args = parser.parse_args()


workspace = args.workspace_id
url = f"https://api.getpostman.com/workspaces/{workspace}"
base_url = args.baseurl
collections_index_file = args.index


with open(args.postmanapikeys, 'r') as f:
    POST_MAN_KEYS = json.load(f)


if isinstance(POST_MAN_KEYS, dict):
    sys.exit("postmanapikeys.json has to be list")
if len(POST_MAN_KEYS) == 0:
    sys.exit("need minimum of one postman api key to begin retrieving information")


def get_response(index, url):
    response = requests.request(
        "GET", url, headers={"X-Api-Key": POST_MAN_KEYS[index]})
    if response.status_code == 429:
        if index < len(POST_MAN_KEYS):
            index += 1
            return get_response(index, url)
        else:
            print('keys provided were exhousted')
            sys.exit(0)
    return response


index = 0
response = get_response(index, url)

data = response.json()
with open(collections_index_file, 'w') as f:
    collections = []
    for collection in data['workspace']['collections']:
        collections.append({
            "collection_id": collection['uid'],
            "name": collection['name'],
            "refer_url": f"{base_url}/collection/{collection['uid']}",
        })
    json.dump(collections, f, indent=4)
