import csv
import re


def convert_csv_to_list(csv_file_path: str) -> list:
    with open(csv_file_path, mode='r', encoding="ISO-8859-9") as file:
        reader = csv.reader(file, delimiter=';')
        for i in range(2):
            next(reader)
        headers = next(reader)
        headers = list(map(parse_string, headers))
        print(headers)
        dict_reader = csv.DictReader(
            file, fieldnames=headers, skipinitialspace=True, delimiter=";")
        return list(dict_reader)

def parse_string(value: str):
    string = value.replace(' ', '_')
    return string.lower()

def dict_search(search_value: str, list_of_dicts: list) -> list:
    found_dicts = []
    compiled_re = re.compile(search_value, re.IGNORECASE)
    for iter_dict in list_of_dicts:
        if re.search(compiled_re, str(iter_dict.values())):
            found_dicts.append(iter_dict)
    return found_dicts
