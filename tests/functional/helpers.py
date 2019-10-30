import json
import os


def load_payload(name):
    filename = os.path.join(os.path.dirname(__file__), f"payloads/{name}.json")
    with open(filename) as json_file:
        return json.load(json_file)
