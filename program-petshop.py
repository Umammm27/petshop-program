import time

data_barang = {
    "K0001": {"namaBarang": "cat wetfood", "kategoriHewan": "kucing", "merk": "wiskas", "harga": 20000, "diskon": 10, "stok": 2},
    "A0001": {"namaBarang": "sampo anjing", "kategoriHewan": "anjing", "merk": "lifedoug", "harga": 35000, "diskon": 0, 'stok': 3}
}

# Variabel global untuk menyimpan nama barang dan jumlah stok yang dipilih oleh pelanggan
nama_barang_terpilih = ""
jumlah_stok_terpilih = 0

def pelanggan():
    global nama_barang_terpilih, jumlah_stok_terpilih  # Gunakan variabel global

    while True:
        print("\nSelamat Datang di Petshop Umam :")
        print("1. Lihat Barang")
        print("2. Checkout")
        print("3. Keluar")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            menuTampil()
            break
        elif pilihan == "2":
            if nama_barang_terpilih and jumlah_stok_terpilih > 0:
                checkout()
                break
            else:
                print("Anda belum memilih barang atau jumlah stok kurang dari 1. Silakan pilih barang terlebih dahulu.")
        elif pilihan == "3":
            print("Terima kasih dan Sampai Jumpa Kembali.")
            print('================================================')
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def menuTampil():
  while True:
    print("\nSelamat Datang di Petshop Umam :")
    print("1. Tampilkan Semua Barang ")
    print("2. Tampilkan Berdasarkan Hewan ")
    print('3. Tampilkan Berdasarkan Urutan Harga ')
    print('4. Cari Barang ')
    print("5. Kembali")

    pilihan = input("Pilih opsi (1/2/3/4/5): ")
    if pilihan == "1":
      tampilSemua()
      break
    elif pilihan == "2":
      tampilKategori()
      break
    elif pilihan == '3':
      tampilUrut()
      break
    elif pilihan == '4':
      cari()
      break
    elif pilihan == "5":
      pelanggan()
      break
    else:
      print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def tampilSemua():
    global nama_barang_terpilih, jumlah_stok_terpilih  # Gunakan variabel global

    while True:
        print("\nDaftar Barang di Petshop:")
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
        for id_barang, barang in data_barang.items():
            print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))

        pilihan = input("Beli Barang (Y/N) : ")
        pilihan = pilihan.lower()

        if pilihan == "y":
            beli = input('Masukkan Nama Barang : ')
            if beli in [barang["namaBarang"] for barang in data_barang.values()]:
                nama_barang_terpilih = beli
                while True:
                    try:
                        jumlah_stok_terpilih = int(input(f"Masukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                        if jumlah_stok_terpilih <= 0:
                            print("Jumlah stok harus lebih dari 0.")
                        elif jumlah_stok_terpilih > data_barang[id_barang]["stok"]:
                            print(f"Stok tidak mencukupi. Stok tersedia: {data_barang[id_barang]['stok']}.")
                        else:
                            print(f"Anda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                            break
                    except ValueError:
                        print("Masukkan jumlah stok dalam angka.")
            else:
                print(f"Nama barang '{beli}' tidak ditemukan.")
        elif pilihan == 'n':
            menuTampil()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def tampilKategori():
    global nama_barang_terpilih, jumlah_stok_terpilih  # Gunakan variabel global

    while True:
        kategori = input("Masukkan kategori hewan (kucing/anjing): ").lower()  # Memastikan huruf pertama kapital
        if kategori not in ["kucing", "anjing"]:
            print("Mohon maaf. Kami hanya menjual barang untuk 'Kucing' dan 'Anjing'.")
            continue

        print("\nDaftar Barang di Petshop untuk Kategori", kategori, ":")
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
        
        for id_barang, barang in data_barang.items():
            if barang["kategoriHewan"] == kategori:
                print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))

        pilihan = input("Beli Barang (Y/N) : ")
        pilihan = pilihan.lower()

        if pilihan == "y":
            beli = input('Masukkan Nama Barang : ')
            if beli in [barang["namaBarang"] for barang in data_barang.values()]:
                nama_barang_terpilih = beli
                while True:
                    try:
                        jumlah_stok_terpilih = int(input(f"Masukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                        if jumlah_stok_terpilih <= 0:
                            print("Jumlah stok harus lebih dari 0.")
                        else:
                            print(f"Anda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                            break
                    except ValueError:
                        print("Masukkan jumlah stok dalam angka.")
            else:
                print(f"Nama barang '{beli}' tidak ditemukan.")
        elif pilihan == 'n':
            menuTampil()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def tampilUrut():
    global nama_barang_terpilih, jumlah_stok_terpilih  # Gunakan variabel global

    while True:
        print("\nTampilkan Barang di Petshop:")
        print("1. Urutkan Harga dari Rendah ke Tinggi")
        print("2. Urutkan Harga dari Tinggi ke Rendah")
        print("3. Kembali")

        pilihan = input("Pilih opsi (1/2/3): ")
        
        if pilihan == "1":
            # Urutkan data_barang berdasarkan harga dari rendah ke tinggi
            sorted_barang = sorted(data_barang.items(), key=lambda x: x[1]["harga"])
            print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
            for id_barang, barang in sorted_barang:
                print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))
        
        elif pilihan == "2":
            # Urutkan data_barang berdasarkan harga dari tinggi ke rendah
            sorted_barang = sorted(data_barang.items(), key=lambda x: x[1]["harga"], reverse=True)
            print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
            for id_barang, barang in sorted_barang:
                print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))

        elif pilihan == "3":
            menuTampil()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def cari():
    while True:
        nama_barang_cari = input("Masukkan nama barang yang ingin dicari: ").lower()

        if nama_barang_cari in [barang["namaBarang"] for barang in data_barang.values()]:
            print("\nDetail Barang:")
            print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
            for id_barang, barang in data_barang.items():
                if barang["namaBarang"] == nama_barang_cari:
                    print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))

                    pilihan = input("\nBeli Barang (Y/N) : ").lower()
                    if pilihan == "y":
                        global nama_barang_terpilih, jumlah_stok_terpilih  # Gunakan variabel global
                        nama_barang_terpilih = barang["namaBarang"]
                        while True:
                            try:
                                jumlah_stok_terpilih = int(input(f"Masukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                                if jumlah_stok_terpilih <= 0:
                                    print("Jumlah stok harus lebih dari 0.")
                                elif jumlah_stok_terpilih > barang["stok"]:
                                    print(f"Stok tidak mencukupi. Stok tersedia: {barang['stok']}.")
                                else:
                                    print(f"Anda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                                    break
                            except ValueError:
                                print("Masukkan jumlah stok dalam angka.")
                    elif pilihan == "n":
                        menuTampil()
                        return 
                    else:
                        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
                    break
        else:
            print(f"Barang dengan nama '{nama_barang_cari}' tidak tersedia.")
        
        kembali = input("Cari barang lain? (Y/N) : ").lower()
        if kembali != "y":
            menuTampil()
            return  

def checkout():
    global nama_barang_terpilih, jumlah_stok_terpilih  # Gunakan variabel global

    while True:
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon"))
        for id_barang, barang in data_barang.items():
            if barang["namaBarang"] == nama_barang_terpilih:
                print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:}%".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"]))

                # Kurangi jumlah stok barang yang dipilih
                if barang["stok"] >= jumlah_stok_terpilih:
                    barang["stok"] -= jumlah_stok_terpilih
                else:
                    print("Mohon maaf. Stok tidak mencukupi. Stok tersedia: {}".format(barang["stok"]))
                    pelanggan()
                    break

                print(f"Barang {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs) telah dibeli.")

                # Hapus barang jika stok mencapai 0
                if barang["stok"] == 0:
                    del data_barang[id_barang]

                input("Tekan Enter untuk kembali ke menu pelanggan...")
                pelanggan()
                break
        break

def adminLogin():
    while True:
        print("\nSelamat Datang Admin Petshop Umam :")
        print("1. Masukkan Username")
        print("2. Kembali")

        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            username = input('Masukkan Username (Case-Sensitive): ')

            if username == 'umam':
                admin()
                break
            else:
                print('Username Salah!')
                time.sleep(1)
                adminLogin()
        elif pilihan == '2':
            MenuUtama()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def admin():
    while True:
        print('==========Petshop Umam==========')
        print("\nSelamat Datang Admin Petshop Umam :")
        print("Ini Menu Admin")
        break

def MenuUtama():
    while True:
        print("\nSelamat Datang di Petshop Umam :")
        print("1. Pelanggan")
        print("2. Admin")
        print("3. Keluar")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            pelanggan()
            break
        elif pilihan == "2":
            adminLogin()
            break
        elif pilihan == "3":
            print("Terima kasih dan Sampai Jumpa Kembali.")
            print('================================================')
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

print('==========Petshop Umam==========')
MenuUtama()
