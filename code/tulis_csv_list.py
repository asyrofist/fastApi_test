import csv

contacts = []

with open('contacts.csv', mode='a') as csv_file:
    # membuat objek writer
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # menulis baris ke file CSV
    writer.writerow(["5", "Dian", "021100022", "jl.surabaya", "1-Jan-21", "2-Jan-22"])
    writer.writerow(["6", "Meli", "0214444432", "jl.malang", "2-Feb-21", "3-Feb-22"])
    
print("Writing Done!")
