import csv, os, time, datetime

csv_filename = 'contacts.csv'
csv_cuti = 'cuti.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Daftar Kontak")
    print("[2] Buat Kontak Baru")
    print("[3] Edit Kontak")
    print("[4] Hapus Kontak")
    print("[5] Cari Kontak")
    print("[6] Lihat Daftar Cuti")
    print("[0] Exit")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if(selected_menu == "1"):
        show_contact()
    elif(selected_menu == "2"):
        create_contact()
    elif(selected_menu == "3"):
        edit_contact()
    elif(selected_menu == "4"):
        delete_contact()
    elif(selected_menu == "5"):
        search_concat()
    elif(selected_menu == "0"):
        exit()
    elif(selected_menu == "6"):
        show_cuti()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()


def show_cuti():
    clear_screen()
    contacts_kotak = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts_kotak.append(row)

    if (len(contacts_kotak) > 0):
        labels_kontak = contacts_kotak.pop(0)


    contacts_cuti = []
    with open(csv_cuti) as file_csv:
        csv_reader = csv.reader(file_csv, delimiter=",")
        for row in csv_reader:
            contacts_cuti.append(row)

    if (len(contacts_cuti) > 0):
        labels = contacts_cuti.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]} \t\t {labels_kontak[5]} \t\t {labels[3]} \t\t {labels[4]}")
        print("-"*34)
        for data in contacts_cuti:
            for cdata in contacts_kotak:
                waktu1 = time.mktime(datetime.datetime.strptime(cdata[5], "%d/%m/%Y").timetuple())
                waktu2 = time.mktime(datetime.datetime.strptime(data[2], "%d/%m/%Y").timetuple())
                delta = waktu2 - waktu1
                print(f'{data[0]} \t {data[1]} \t\t {data[2]} \t\t {cdata[5]} \t\t {delta} \t\t {data[4]}')
    else:
        print("Tidak ada data!")

    back_to_menu()

def show_contact():
    clear_screen()
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)

    if (len(contacts) > 0):
        labels = contacts.pop(0)
        print(f"{labels[0]} \t {labels[1]} \t\t {labels[2]} \t\t {labels[3]} \t\t {labels[4]} \t\t {labels[5]}")
        print("-"*34)
        for data in contacts:
            print(f'{data[0]} \t {data[1]} \t\t {data[2]} \t\t {data[3]} \t\t {data[4]} \t\t {data[5]}')
    else:
        print("Tidak ada data!")
    back_to_menu()


def create_contact():
    clear_screen()
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA', 'NOMORINDUK', 'ALAMAT', 'TANGGALLAHIR', 'TANGGALBERGABUNG']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        no = input("No urut: ")
        nama = input("Nama lengkap: ")
        telepon = input("No. Induk: ")
        alamat = input("Alamat: ")
        tanggalLahir = input("Tanggal Lahir: ")
        tanggalBergabung = input("Tanggal Bergabung: ")

        writer.writerow({'NO': no, 
                         'NAMA': nama, 
                         'NOMORINDUK': telepon, 
                         'ALAMAT': alamat, 
                         'TANGGALLAHIR': tanggalLahir,    
                         'TANGGALBERGABUNG': tanggalBergabung})    
    
    back_to_menu()


def search_concat():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    no = input("Cari berdasrakan nomer urut> ")

    data_found = []

    # mencari contact
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            data_found = contacts[indeks]
            
        indeks = indeks + 1

    if len(data_found) > 0:
        print("DATA DITEMUKAN: ")
        print(f"Nama: {data_found['NAMA']}")
        print(f"Telepon: {data_found['NOMORINDUK']}")
        print(f"Alamat: {data_found['ALAMAT']}")
        print(f"Tanggal Lahir: {data_found['TANGGALLAHIR']}")
        print(f"Tanggal Bergabung: {data_found['TANGGALBERGABUNG']}")
    else:
        print("Tidak ada data ditemukan")
    back_to_menu()
    


def edit_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t NOMORINDUK \t\t ALAMAT \t\t TANGGALLAHIR \t\t TANGGALBERGABUNG")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['NOMORINDUK']} \t {data['ALAMAT']} \t {data['TANGGALLAHIR']} \t {data['TANGGALBERGABUNG']}")

    print("-----------------------")
    no = input("Pilih nomer kontak> ")
    nama = input("nama baru: ")
    telepon = input("nomer induk baru: ")
    alamat = input("alamat baru: ")
    tanggalLahir = input("tanggal lahir baru: ")
    tanggalBergabung = input("tanggal Bergabung: ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts[indeks]['NAMA'] = nama
            contacts[indeks]['NOMORINDUK'] = telepon
            contacts[indeks]['ALAMAT'] = telepon
            contacts[indeks]['TANGGALLAHIR'] = tanggalLahir
            contacts[indeks]['TANGGALBERGABUNG'] = tanggalBergabung
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'NOMORINDUK', 'ALAMAT', 'TANGGALLAHIR', 'TANGGALBERGABUNG']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 
                             'NAMA': new_data['NAMA'], 
                             'NOMORINDUK': new_data['NOMORINDUK'], 
                             'ALAMAT': new_data['ALAMAT'], 
                             'TANGGALLAHIR': new_data['TANGGALLAHIR'], 
                             'TANGGALBERGABUNG': new_data['TANGGALBERGABUNG']}) 

    back_to_menu()



def delete_contact():
    clear_screen()
    contacts = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            contacts.append(row)

    print("NO \t NAMA \t\t NOMORINDUK \t\t ALAMAT \t\t TANGGALLAHIR \t\t TANGGALBERGABUNG")
    print("-" * 32)

    for data in contacts:
        print(f"{data['NO']} \t {data['NAMA']} \t {data['NOMORINDUK']} \t {data['ALAMAT']} \t {data['TANGGALLAHIR']} \t {data['TANGGALBERGABUNG']}")

    print("-----------------------")
    no = input("Hapus nomer> ")

    # mencari contact dan mengubah datanya
    # dengan data yang baru
    indeks = 0
    for data in contacts:
        if (data['NO'] == no):
            contacts.remove(contacts[indeks])
        indeks = indeks + 1

    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA', 'NOMORINDUK', 'ALAMAT', 'TANGGALLAHIR', 'TANGGALBERGABUNG']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in contacts:
            writer.writerow({'NO': new_data['NO'], 
            'NAMA': new_data['NAMA'], 
            'NOMORINDUK': new_data['NOMORINDUK'], 
            'ALAMAT': new_data['ALAMAT'], 
            'TANGGALLAHIR': new_data['TANGGALLAHIR'], 
            'TANGGALBERGABUNG': new_data['TANGGALBERGABUNG']}) 

    print("Data sudah terhapus")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()