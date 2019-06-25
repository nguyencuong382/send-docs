import json


def load_json(path):
    with open(path, 'r') as json_file:
        content = json.load(json_file)
    return content
