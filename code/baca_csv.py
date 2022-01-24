import csv

with open('contacts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    for data in csv_reader:
            print(data)
