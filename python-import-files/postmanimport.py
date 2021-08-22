import requests
import json
import sys
import tempfile
from dotextensions.server.handlers.postman2http import ImportPostmanCollection, Command
from dotextensions.server.utils import clean_filename
import pathlib

package_dir = pathlib.Path(__file__).parent
with open(package_dir.joinpath(".postmanapikeys.json"), 'r') as f:
    POST_MAN_KEYS = json.load(f)


def get_response(index, url):
    response = requests.request(
        "GET", url, headers={"X-Api-Key": POST_MAN_KEYS[index]})
    if response.status_code == 429:
        if index < len(POST_MAN_KEYS):
            index += 1
            return get_response(index, url)
        else:
            print('all keys exhousted')
            sys.exit(0)
    return response


START_FROM = 0

if len(sys.argv) == 2:
    collections_index_root = sys.argv[1]
else:
    collections_index_root = package_dir.joinpath("collections.index.json")


def main():
    index_key = 0
    collections_root = package_dir.parent.joinpath(
        "../collections")
    with open(collections_index_root, 'r') as postman_collection_index_file2:
        data = json.load(postman_collection_index_file2)
        with tempfile.TemporaryDirectory() as tmpdirname:
            for index, collection_metadata in enumerate(data):
                name = collection_metadata["name"]
                collection_id = collection_metadata["collection_id"]
                referral_url = collection_metadata["refer_url"]
                url = f"https://api.getpostman.com/collections/{collection_id}"
                print(f'running for {collection_id} count: {index}')
                # create temp dir
                postman_collection_filename = tmpdirname + "/" + \
                    collection_id + ".postman_collection.json"
                if index < START_FROM:
                    continue
                with open(postman_collection_filename, mode='w') as temp_postman_collection:
                    response = get_response(index_key, url)
                    collection = response.json()['collection']
                    temp_postman_collection.write(
                        json.dumps(collection, indent=True))
                    print(f'completed {name} {collection_id}')
                postman_importer = ImportPostmanCollection()
                postman_importer.run(
                    command=Command(method="/import/postman",
                                    params={
                                        "link": postman_collection_filename,
                                        "save": True,
                                        "overwrite": True,
                                        "directory": str(collections_root.absolute())
                                    },
                                    id=1
                                    )
                )
                postman_info = collections_root.joinpath(clean_filename(
                    collection['info']['name']), "POSTMAN_INFO.md")
                postman_info.parent.mkdir(parents=True, exist_ok=True)
                print(postman_info)
                with open(postman_info, mode='w') as f:
                    f.write(f"""imported from {referral_url}
collectionId: {collection_id}
name: {name}""")


if __name__ == '__main__':
    main()
