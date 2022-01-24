import csv

contacts = []

with open('contacts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        contacts.append(row)


labels = contacts.pop(0)

#print(labels)
#print(contacts)

print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]} \t\t {labels[3]} \t\t {labels[4]} \t\t {labels[4]}')
print("-"*34)
for data in contacts:
    print(f'{data[0]} \t {data[1]} \t\t {data[2]} \t\t {data[3]} \t\t {data[4]} \t\t {data[5]}')
