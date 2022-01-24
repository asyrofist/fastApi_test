import csv

with open('contacts.csv', mode='a') as csv_file:
    # menentukan label
    fieldnames = ['NO', 'NAMA', 'NOMORINDUK', 'ALAMAT', 'TANGGALLAHIR', 'TANGGALBERGABUNG']
    
    # membuat objek writer
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # menulis baris ke file CSV
    writer.writeheader()
    writer.writerow({'NO': '10', 'NAMA': 'Via Vallen', 'NOMORINDUK': '02109999', 'ALAMAT': 'jl. surabaya', 'TANGGALLAHIR': '1-JAN-21', 'TANGGALBERGABUNG': '2-JAN-22'})
    writer.writerow({'NO': '11', 'NAMA': 'M. Andi', 'NOMORINDUK': '02148488888', 'ALAMAT': 'jl. malang', 'TANGGALLAHIR': '2-FEB-21', 'TANGGALBERGABUNG': '3-FEB-22'})
    
print("Writing Done!")
