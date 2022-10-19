import csv
import os.path


def get_structure_row():
    row = {
        'first_name': '',
        'second_name': '',
        'phone': '',
        'description': '',
    }
    return row


def read_file(file="data.csv"):
    data = []
    fieldnames = ['first_name', 'second_name', 'phone', 'description']
    if not os.path.exists(file):
        with open(file, 'w', newline="", encoding="utf-8") as csvfile:
            csvfile.write('')

    with open(file, 'r', newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";", fieldnames=fieldnames)
        for row in reader:
            data.append(dict(row))
    return data


def save_file_row(row):
    fieldnames = ['first_name', 'second_name', 'phone', 'description']
    if not os.path.exists("data.csv"):
        with open("data.csv", 'w', newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=fieldnames)
            writer.writeheader()

    with open("data.csv", 'a', newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([row['first_name'], row['second_name'], row['phone'], row['description']])


def save_file(data, file="data.csv"):

    with open(file, 'w', newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in data:
            writer.writerow([row['first_name'], row['second_name'], row['phone'], row['description']])
