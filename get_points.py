import csv


def read_csv(file_name=None):
    if file_name is None:
        file_name = 'csv/test.csv'

    response = []
    with open(file_name, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            response.append(row)

    return response
