import csv

contacts = []

with open('contacts.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        contacts.append(row)



print("NO \t NAMA \t\t NOMORINDUK \t\t ALAMAT \t\t TANGGALLAHIR \t\t TANGGALBERGABUNG")
print("-" * 32)

for data in contacts:
    print(f"{data['NO']} \t {data['NAMA']} \t\t {data['NOMORINDUK']} \t\t {data['ALAMAT']} \t\t {data['TANGGALLAHIR']} \t\t {data['TANGGALBERGABUNG']}")
