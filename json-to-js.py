import glob
import os
import json
from pprint import pprint


def get_json_files(search_folder):
    files = glob.glob(search_folder + "*.json")
    print(files)

    for json_file in files:
        json_to_js(search_folder, json_file)


def json_to_js(search_folder, json_file):
    js_file = json_file.replace(".json", ".js")

    with open(json_file) as fin, open(js_file, "w") as fout:
        data = json.load(fin)
        script = data["index.js"].split("\n")

        for line in script:
            fout.write(line + "\n")

        pprint(script)


if __name__ == "__main__":
    search_dir = "D:\\\Projects\\Python\\freecodecamp-json-to-js\\files\\"

    get_json_files(search_dir)
