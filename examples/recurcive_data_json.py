
"""
    How to get recursive data form a json file
"""
import json
import os


def extract_values(json_object, json_key):
    match json_object:
        case json_object if isinstance(json_object, dict):
            for key, value in json_object.items():
                if key == json_key:
                    yield value
                elif isinstance(value, (dict, list)):
                    yield from extract_values(value, json_key)

        case json_object if isinstance(json_object, list):
            for value in json_object:
                yield from extract_values(value, json_key)


# if isinstance(json_object, dict):
#     for key, value in json_object.items():
#         if key == json_key:
#             yield value
#         elif isinstance(value, (dict, list)):
#             yield from extract_values(value, json_key)
# elif isinstance(json_object, list):
#     for value in json_object:
#         yield from extract_values(value, json_key)


with open(os.path.join('../resources/data.json')) as json_file:
    json_dict = json.loads(json_file.read())  # .decode("utf-8")

    for data in extract_values(json_dict, 'value'):
        print(data)
