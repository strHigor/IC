from csv import DictReader

def convert_csv_to_list(csv_file_path: str):
    with open(csv_file_path, mode='r', encoding='ISO-8859-9') as file:
        return list(DictReader(file))