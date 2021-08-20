import os
import pathlib
import traceback

collections_list = pathlib.Path("./collections")
with open("README.md", 'w') as readmefile:
    readmefile.write("""name | dothttp-link | postman link
---- | ----- | -----
""")

    for col in os.listdir(collections_list):
        # print(col)
        try:
            with open(os.path.join(collections_list, col, "POSTMAN_INFO.md"), 'r') as f:
                link = f.readline()
                collection_id = f.readline()
                name = f.read()
                link = link[len("imported from "):]
                name = name[len("name: "):].replace("\n", "\t")
                readmefile.write(
                    f" {name} | [dothttp](collections/{col}) | [postman]({link.strip()}) | \n")
        except:
            print(col)
            traceback.print_exc()
