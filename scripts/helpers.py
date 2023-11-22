import datetime
import json
from functools import reduce
from operator import getitem


DATETIME_STR_FORMAT = "%Y-%m-%d_%H:%M:%S.%f"


def get_now_string() -> str:
    return datetime.datetime.now().strftime(DATETIME_STR_FORMAT)


# def get_config(config_filepath: str) -> dict:
#     with open(config_filepath) as f:
#         config = json.load(f)
#     return config


def get_config(config_filepath) -> dict:
    with open(config_filepath, "r") as file:
        config = json.load(file)
    return config


def get_json(json_filepath) -> dict:
    with open(json_filepath, "r") as file:
        json_data = json.load(file)
        return json_data


def update_json(json_filepath: str, nested_parameter: str, new_value):
    try:
        with open(json_filepath, "r") as file:
            json_data = json.load(file)

        keys = nested_parameter.split(".")
        nested_data = json_data
        for key in keys[:-1]:
            nested_data = nested_data[key]
        nested_data[keys[-1]] = new_value

        with open(json_filepath, "w") as file:
            json.dump(json_data, file, indent=2)

        print(f"Updated '{nested_parameter}' in {json_filepath}' to '{new_value}'")
    except FileNotFoundError:
        print(f"Error: File '{json_filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{json_filepath}': {e}")
    except KeyError:
        print(f"Error: Nested parameter '{nested_parameter}' not found in JSON.")
