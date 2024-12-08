import yaml
from time import time, sleep
import json




def update_scratchpad(messages, pad, max):
    if len(messages) > max:
        messages.pop(0)
    pad = '\n\n'.join(messages).strip()
    return pad


def stringify_convo_json(role_content_json):
    for item in role_content_json:
        stringified_json = ''.join(f"Role: {item['role']}, Content: {item['content']}")
    return stringified_json


def save_yaml(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

def write_json(json_object, indent, filepath):
    writeable_json = json.dumps(json_object, indent=indent)
    with open(filepath, "w") as outfile:
        outfile.write(writeable_json)
