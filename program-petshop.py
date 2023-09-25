import time

data_barang = {
    "K0001": {"namaBarang": "cat wetfood", "kategoriHewan": "kucing", "merk": "wiskas", "harga": 20000, "diskon": 10, "stok": 2},
    "A0001": {"namaBarang": "sampo anjing", "kategoriHewan": "anjing", "merk": "lifedoug", "harga": 35000, "diskon": 20, 'stok': 3},
    "K0002": {"namaBarang": "cat dryfood", "kategoriHewan": "kucing", "merk": "wiskas", "harga": 40000, "diskon": 10, "stok": 8},
    "K0003": {"namaBarang": "sampo kucing", "kategoriHewan": "kucing", "merk": "lifecat", "harga": 30000, "diskon": 0, "stok": 5},
    "K0004": {"namaBarang": "mainan kucing", "kategoriHewan": "kucing", "merk": "catlego", "harga": 15000, "diskon": 10, "stok": 10},
    "A0002": {"namaBarang": "susu anjing", "kategoriHewan": "anjing", "merk": "dogmilk", "harga": 15000, "diskon": 10, 'stok': 5},
    "A0003": {"namaBarang": "dog wetfood", "kategoriHewan": "anjing", "merk": "dog choicez", "harga": 60000, "diskon": 5, 'stok': 8},
    "A0004": {"namaBarang": "vitamin anjing", "kategoriHewan": "anjing", "merk": "Dog-fit", "harga": 100000, "diskon": 0, 'stok': 10},
}

nama_barang_terpilih = ""
jumlah_stok_terpilih = 0
kategori_terpilih = ""



def hitungDiskon(harga, diskon):
    return harga - (harga * diskon / 100)


def pelanggan():
    global nama_barang_terpilih, jumlah_stok_terpilih  

    while True:
        print("\nSelamat Datang di Petshop Umam :")
        print("\n[1]. Lihat Barang")
        print("\n[2]. Checkout")
        print("\n[3]. Keluar")

        pilihan = input("\nPilih opsi (1/2/3): ")

        if pilihan == "1":
            menuTampil()
            break
        elif pilihan == "2":
            if nama_barang_terpilih and jumlah_stok_terpilih > 0:
                checkout()
                break
            else:
                print("\nAnda belum memilih barang atau jumlah stok kurang dari 1. Silakan pilih barang terlebih dahulu.")
        elif pilihan == "3":
            print("\nTerima kasih dan Sampai Jumpa Kembali.")
            print('\n================================================')
            time.sleep(1)
            menuUtama()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def menuTampil():
  while True:
    print("\nSelamat Datang di Petshop Umam :")
    print("\n[1]. Tampilkan Semua Barang ")
    print("\n[2]. Tampilkan Berdasarkan Hewan ")
    print('\n[3]. Tampilkan Berdasarkan Urutan Harga ')
    print('\n[4]. Cari Barang ')
    print("\n[5]. Kembali")

    pilihan = input("\nPilih opsi (1/2/3/4/5): ")
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
      print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def tampilSemua():
    global nama_barang_terpilih, jumlah_stok_terpilih  

    while True:
        print("\nDaftar Barang di Petshop:")
        header = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok")
        print("\n" + header)
        print("-" * len(header)) 

        for id_barang, barang in data_barang.items():
            row = "{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], str(barang["diskon"])+'%', barang["stok"])
            print(row)

        print("-" * len(header))

        pilihan = input("\nIngin membeli sesuatu? (Y/N) : ").lower()

        if pilihan == "y":
            beli = input('\nMasukkan Nama Barang : ')
            id_barang_terpilih = None 

            for id_barang, barang in data_barang.items():
                if barang["namaBarang"] == beli:
                    id_barang_terpilih = id_barang
                    break

            if id_barang_terpilih is not None:
                nama_barang_terpilih = beli
                while True:
                    try:
                        jumlah_stok_terpilih = int(input(f"\nMasukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                        if jumlah_stok_terpilih <= 0:
                            print("\nJumlah stok harus lebih dari 0.")
                        elif jumlah_stok_terpilih > data_barang[id_barang_terpilih]["stok"]:
                            print(f"\nStok tidak mencukupi. Stok tersedia: {data_barang[id_barang_terpilih]['stok']}.")
                        else:
                            print(f"\nAnda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                            print('\nTerimakasih telah berbelanja di toko kami!')
                            time.sleep(0.5)
                            break
                    except ValueError:
                        print("\nMohon Maaf. Masukkan jumlah stok dalam angka.")
                checkout()
                break
            else:
                print(f"\nMohon Maaf. Nama barang '{beli}' tidak ditemukan.")

        elif pilihan == 'n':
            menuTampil()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def tampilKategori():
    global nama_barang_terpilih, jumlah_stok_terpilih, kategori_terpilih

    while True:
        kategori = input("\nMasukkan kategori hewan (kucing/anjing): ").lower()  
        if kategori not in ["kucing", "anjing"]:
            print("\nMohon maaf. Kami hanya menjual barang untuk 'Kucing' dan 'Anjing'.")
            continue

        kategori_terpilih = kategori

        print("\nDaftar Barang di Petshop untuk Kategori", kategori_terpilih, ":")
        header = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok")
        print("\n" + header)
        print("-" * len(header)) 
        
        for id_barang, barang in data_barang.items():
            if barang["kategoriHewan"] == kategori_terpilih:
                row = "{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], str(barang["diskon"])+'%', barang["stok"])
                print(row)
                
        print("-" * len(header))
        
        pilihan = input("\nIngin membeli sesuatu? (Y/N) : ").lower()

        if pilihan == "y":
            beli = input('\nMasukkan Nama Barang : ')
            id_barang_terpilih = None 

            for id_barang, barang in data_barang.items():
                if barang["namaBarang"] == beli:
                    id_barang_terpilih = id_barang
                    break

            if id_barang_terpilih is not None:
                if data_barang[id_barang_terpilih]["kategoriHewan"] == kategori_terpilih:
                    while True:
                        try:
                            jumlah_stok_terpilih = int(input(f"\nMasukkan jumlah stok {beli} yang akan dibeli: "))
                            if jumlah_stok_terpilih <= 0:
                                print("\nJumlah stok harus lebih dari 0.")
                            elif jumlah_stok_terpilih > data_barang[id_barang_terpilih]["stok"]:
                                print(f"\nStok tidak mencukupi. Stok tersedia: {data_barang[id_barang_terpilih]['stok']}.")
                            else:
                                print(f"\nAnda telah memilih {beli} ({jumlah_stok_terpilih} pcs).")
                                print('\nTerimakasih telah berbelanja di toko kami!')
                                time.sleep(0.5)
                                break
                        except ValueError:
                            print("\nMohon Maaf. Masukkan jumlah stok dalam angka.")
                    
                    checkout()
                    break
                else:
                    print(f"\nBarang '{beli}' tidak tersedia di kategori {kategori_terpilih}.")
            else:
                print(f"\nMohon Maaf. Nama barang '{beli}' tidak ditemukan.")

        elif pilihan == 'n':
            menuTampil()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def tampilUrut():
    global nama_barang_terpilih, jumlah_stok_terpilih 

    while True:
        print("\nTampilkan Barang di Petshop:")
        print("\n[1]. Urutkan Harga dari Rendah ke Tinggi")
        print("\n[2]. Urutkan Harga dari Tinggi ke Rendah")
        print("\n[3]. Kembali")

        pilihan = input("\nPilih opsi (1/2/3): ")
        
        if pilihan == "1":
            sorted_barang = sorted(data_barang.items(), key=lambda x: x[1]["harga"])
            print("\nDaftar Barang di Petshop:")
            header = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok")
            print("\n" + header)
            print("-" * len(header)) 
            for id_barang, barang in sorted_barang:
                row = "{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], str(barang["diskon"])+'%', barang["stok"])
                print(row)

            print("-" * len(header))
            
            pilihanbeli1 = input("\nIngin membeli sesuatu? (Y/N) : ").lower()

            if pilihanbeli1 == "y":
                beli = input('\nMasukkan Nama Barang : ')
                id_barang_terpilih = None 

                for id_barang, barang in data_barang.items():
                    if barang["namaBarang"] == beli:
                        id_barang_terpilih = id_barang
                        break

                if id_barang_terpilih is not None:
                    nama_barang_terpilih = beli
                    while True:
                        try:
                            jumlah_stok_terpilih = int(input(f"\nMasukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                            if jumlah_stok_terpilih <= 0:
                                print("\nJumlah stok harus lebih dari 0.")
                            elif jumlah_stok_terpilih > data_barang[id_barang_terpilih]["stok"]:
                                print(f"\nStok tidak mencukupi. Stok tersedia: {data_barang[id_barang_terpilih]['stok']}.")
                            else:
                                print(f"\nAnda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                                print('\nTerimakasih telah berbelanja di toko kami!')
                                time.sleep(0.5)
                                break
                        except ValueError:
                            print("\nMohon Maaf. Masukkan jumlah stok dalam angka.")
                    checkout()
                    break
                else:
                    print(f"\nMohon Maaf. Nama barang '{beli}' tidak ditemukan.")

                
            elif pilihanbeli1 == 'n':
                menuTampil()
                break
            else:
                print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
                
        elif pilihan == "2":
            sorted_barang = sorted(data_barang.items(), key=lambda x: x[1]["harga"], reverse=True)
            print("\nDaftar Barang di Petshop:")
            header = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok")
            print("\n" + header)
            print("-" * len(header)) 
            for id_barang, barang in sorted_barang:
                row = "{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], str(barang["diskon"])+'%', barang["stok"])
                print(row)

            print("-" * len(header))
            
            pilihanBeli2 = input("\nIngin membeli sesuatu? (Y/N) : ").lower()

            if pilihanBeli2 == "y":
                beli = input('\nMasukkan Nama Barang : ')
                id_barang_terpilih = None 

                for id_barang, barang in data_barang.items():
                    if barang["namaBarang"] == beli:
                        id_barang_terpilih = id_barang
                        break

                if id_barang_terpilih is not None:
                    nama_barang_terpilih = beli
                    while True:
                        try:
                            jumlah_stok_terpilih = int(input(f"\nMasukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                            if jumlah_stok_terpilih <= 0:
                                print("\nJumlah stok harus lebih dari 0.")
                            elif jumlah_stok_terpilih > data_barang[id_barang_terpilih]["stok"]:
                                print(f"\nStok tidak mencukupi. Stok tersedia: {data_barang[id_barang_terpilih]['stok']}.")
                            else:
                                print(f"\nAnda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                                print('\nTerimakasih telah berbelanja di toko kami!')
                                time.sleep(0.5)
                                break
                        except ValueError:
                            print("\nMohon Maaf. Masukkan jumlah stok dalam angka.")
                            
                    checkout()
                    break
                else:
                    print(f"\nMohon Maaf. Nama barang '{beli}' tidak ditemukan.")

                
            elif pilihanBeli2 == 'n':
                menuTampil()
                break
            else:
                print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
        elif pilihan == "3":
            menuTampil()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def cari():
    while True:
        nama_barang_cari = input("\nMasukkan nama barang yang ingin dicari: ").lower()

        if nama_barang_cari in [barang["namaBarang"] for barang in data_barang.values()]:
            print("\nDetail Barang:")
            header = "{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok")
            print("\n" + header)
            print("-" * len(header)) 
            for id_barang, barang in data_barang.items():
                if barang["namaBarang"] == nama_barang_cari:
                    row = "{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], str(barang["diskon"])+'%', barang["stok"])
                    print(row)
                    
                    pilihan = input(f"\nIngin membeli {nama_barang_cari}? (Y/N) : ").lower()
                    
                    if pilihan == "y":
                        global nama_barang_terpilih, jumlah_stok_terpilih 
                        nama_barang_terpilih = barang["namaBarang"]
                        while True:
                            try:
                                jumlah_stok_terpilih = int(input(f"\nMasukkan jumlah stok {nama_barang_terpilih} yang akan dibeli: "))
                                if jumlah_stok_terpilih <= 0:
                                    print("\nJumlah stok harus lebih dari 0.")
                                elif jumlah_stok_terpilih > barang["stok"]:
                                    print(f"\nMohon Maaf. Stok tidak mencukupi. Stok tersedia: {barang['stok']}.")
                                else:
                                    print(f"\nAnda telah memilih {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs).")
                                    print('\nTerimakasih telah berbelanja di toko kami!')
                                    time.sleep(0.5)
                                    break
                            except ValueError:
                                print("\nMohon Maaf. Masukkan jumlah stok dalam angka.")
                    
                        checkout()
                        return
                    elif pilihan == "n":
                        menuTampil()
                        return 
                    else:
                        print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
                    break
        else:
            print(f"\nBarang dengan nama '{nama_barang_cari}' tidak tersedia.")
        
        kembali = input("\nCari barang yang lain? (Y/N) : ").lower()
        
        if kembali == "y":
            cari()
            return
        elif kembali == 'n':
            menuTampil()
            return
        else:
            print('\nPilihan tidak valid. Silakan pilih opsi yang benar.')


def checkout():
    global nama_barang_terpilih, jumlah_stok_terpilih

    print("\nDaftar Barang dibeli:")
    header = "{:<5} {:<15} {:<15} {:<10} {:<10} {:<5} {:<15} {:<15} {:<15}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Diskon", "Stok", "Harga Awal","Harga Diskon", "Total Harga")
    print("\n" + header)
    print("-" * len(header))

    for id_barang, barang in data_barang.items():
        if barang["namaBarang"] == nama_barang_terpilih:
            harga = barang["harga"]
            diskon = barang["diskon"]
            harga_diskon = hitungDiskon(harga, diskon)
            harga_total = harga_diskon * jumlah_stok_terpilih
            row = "{:<5} {:<15} {:<15} {:<10} {:<10} {:<5} {:<15} {:<15} {:<15}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"],str(barang["diskon"])+'%',barang["stok"], barang["harga"], harga_diskon, harga_total)
            print(row)

            if barang["stok"] >= jumlah_stok_terpilih:
                barang["stok"] -= jumlah_stok_terpilih
            else:
                print("\nMohon maaf. Stok tidak mencukupi. Stok tersedia: {}".format(barang["stok"]))

            print(f"\nTerima Kasih. Barang {nama_barang_terpilih} ({jumlah_stok_terpilih} pcs) telah dibeli.")

            if barang["stok"] == 0:
                del data_barang[id_barang]

            input("\nTekan Enter untuk kembali ke menu pelanggan...")
            
            nama_barang_terpilih = 0
            
            pelanggan()

            return
    else:
        print('\n--------------------------------------------Data Barang Kosong---------------------------------------------------')
        pelanggan()
        return

def tampilAdmin():
    global nama_barang_terpilih, jumlah_stok_terpilih

    while True:
        print("\nDaftar Barang di Petshop:")
        print("\n{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
        for id_barang, barang in data_barang.items():
            print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))

        pilihan = input("\nTambahkan Barang (Y/N) : ")
        pilihan = pilihan.lower()

        if pilihan == "y":
            tambahItem()
            break
        elif pilihan == 'n':
            admin()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def tambahItem():
    while True:
        print("\nTambah Item")
        nama_barang = input("\nMasukkan nama barang: ")
        
        if any(item['namaBarang'] == nama_barang for item in data_barang.values()):
            print(f"\nData dengan nama barang '{nama_barang}' sudah ada.")
            continue
        
        kategori_hewan = input("Masukkan kategori hewan (Masukkan Anjing/Kucing): ")
        if kategori_hewan in ['kucing','anjing']:
            
            merk = input("Masukkan merk: ")
            
            while True:
                harga_input = input("Masukkan harga: ")
                if harga_input.isdigit():
                    harga = int(harga_input)
                    break
                else:
                    print("Harga harus berupa angka.")
                    
            while True:
                diskon_input = input("Masukkan diskon: ")
                if diskon_input.isdigit():
                    diskon = int(diskon_input)
                    break
                else:
                    print("Diskon harus berupa angka.")
                    
            while True:
                stok_input = input("Masukkan stok: ")
                if stok_input.isdigit():
                    stok = int(stok_input)
                    break
                else:
                    print("Stok harus berupa angka.")

            if "kucing" in kategori_hewan.lower():
                tipe_index = "K"
            else :
                tipe_index = "A"
        else:
            print('\nMohon Masukkan Kategori Kucing / Anjing')
            tambahItem()

        max_kode_barang = max([k for k in data_barang.keys() if k.startswith(tipe_index)], default=tipe_index + "0000")
        max_number = int(max_kode_barang[1:])
        new_number = max_number + 1
        kode_barang = f"{tipe_index}{new_number:04d}"

        
        item_baru = {
            "namaBarang": nama_barang,
            "kategoriHewan": kategori_hewan,
            "merk": merk,
            "harga": harga,
            "diskon": diskon,
            "stok": stok
        }

        data_barang[kode_barang] = item_baru

        print(f"\nItem dengan kode {kode_barang} berhasil ditambahkan.")
        input("\nTekan Enter untuk kembali ke menu admin...")
        admin()
        return

def editItem():
    while True:
        print("\nDaftar Barang di Petshop:")
        print("\n{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
        for id_barang, barang in data_barang.items():
            print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))
    
        print('\n[1]. Masukkan Kode Barang')
        print("\n[2]. Kembali")
        
        pilihan = input("\nPilih opsi (1/2): ")
        if pilihan == "1":
            kode_barang_ubah = input("\nMasukkan kode barang yang ingin diubah: ").upper()
            
            if kode_barang_ubah in data_barang:
                print("\nData Barang yang akan diubah:")
                print("Kode Barang:", kode_barang_ubah)
                print("Nama Barang:", data_barang[kode_barang_ubah]["namaBarang"])
                print("Kategori Hewan (Masukkan Anjing/Kucing):", data_barang[kode_barang_ubah]["kategoriHewan"])
                print("Merk:", data_barang[kode_barang_ubah]["merk"])
                print("Harga:", data_barang[kode_barang_ubah]["harga"])
                print("Diskon:", data_barang[kode_barang_ubah]["diskon"])
                print("Stok:", data_barang[kode_barang_ubah]["stok"])

                if kode_barang_ubah.startswith("K"):
                    kategori_hewan = "kucing"
                elif kode_barang_ubah.startswith("A"):
                    kategori_hewan = "anjing"
                else:
                    kategori_hewan = "Kategori Tidak Diketahui"
                
                print("\nMasukkan informasi baru (kosongkan jika tidak ingin mengubah):")
                nama_barang_baru = input("Nama Barang Baru: ")
                merk_baru = input("Merk Baru: ")
                while True:
                    harga_input_baru = input("Masukkan harga: ")
                    if harga_input_baru.isdigit():
                        harga_baru = int(harga_input_baru)
                        break
                    else:
                        print("Harga harus berupa angka.")
                while True:
                    diskon_input_baru = input("Masukkan diskon: ")
                    if diskon_input_baru.isdigit():
                        diskon_baru = int(diskon_input_baru)
                        break
                    else:
                        print("Diskon harus berupa angka.")
                while True:
                    stok_input_baru = input("Masukkan jumlah stok: ")
                    if stok_input_baru.isdigit():
                        stok_baru = int(stok_input_baru)
                        break
                    else:
                        print("Stok harus berupa angka.")
                        
                konfirmasi = input(f"Apakah Anda yakin ingin mengubah barang dengan kode {kode_barang_ubah}? (Y/N): ")
                if konfirmasi.lower() == 'y':
                    if nama_barang_baru:
                        data_barang[kode_barang_ubah]["namaBarang"] = nama_barang_baru
                    if kategori_hewan:
                        data_barang[kode_barang_ubah]["kategoriHewan"] = kategori_hewan
                    if merk_baru:
                        data_barang[kode_barang_ubah]["merk"] = merk_baru
                    if harga_input_baru:
                        data_barang[kode_barang_ubah]["harga"] = int(harga_baru)
                    if diskon_input_baru:
                        data_barang[kode_barang_ubah]["diskon"] = int(diskon_baru)
                    if stok_input_baru:
                        data_barang[kode_barang_ubah]["stok"] = int(stok_baru)
                
                    print("\nData Barang berhasil diubah.")
                    admin()
                    return
                elif konfirmasi.lower() == 'n':
                    print("\nPengubahan dibatalkan.")
                else:
                    print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
                                
            else:
                print("Kode barang tidak ditemukan. Silakan coba lagi.")
        elif pilihan == "2":
            admin()
            return
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

def hapus():
    while True:
        print("\n[1]. Hapus Berdasarkan ID ")
        print("\n[2]. Hapus Berdasarkan Kategori Hewan ")
        print('\n[3]. Kembali ')
        
        pilihan = input("\nPilih opsi (1/2/3): ")

        if pilihan == "1":
            hapusIndexItem()
            break
        elif pilihan == "2":
            hapusKategori()
            break
        elif pilihan == "3":
            admin()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
            
def hapusKategori():
    while True:
        global nama_barang_terpilih
        global jumlah_stok_terpilih
        
        kategori_yang_dihapus = input("\nMasukkan kategori hewan yang ingin dihapus: ").lower()
        
        item_dihapus = []
        
        for kode_barang, barang in data_barang.items():
            if barang["kategoriHewan"].lower() == kategori_yang_dihapus:
                item_dihapus.append(kode_barang)
        
        if kategori_yang_dihapus in ['kucing','anjing']:
            konfirmasi = input(f"\nApakah Anda yakin ingin menghapus barang dengan kategori {kategori_yang_dihapus}? (Y/N): ")
            if konfirmasi.lower() == 'y':
                for kode_barang in item_dihapus:
                    nama_barang_terpilih = data_barang[kode_barang]["namaBarang"]
                    jumlah_stok_terpilih = data_barang[kode_barang]["stok"]
                    
                    del data_barang[kode_barang]
                    
                    print(f"Item {nama_barang_terpilih} ({jumlah_stok_terpilih} stok) dengan kategori {kategori_yang_dihapus} telah dihapus.")
            elif konfirmasi.lower() == 'n':
                print("\nPenghapusan dibatalkan.")
            else:
                print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
        else:
            print('\nMohon Masukkan Kategori Kucing / Anjing')
            hapusKategori()
            
        admin()
        return
        
def hapusIndexItem():
    while True :
        print("\nDaftar Barang di Petshop:")
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Nama Barang", "Kategori Hewan", "Merk", "Harga", "Diskon", "Stok"))
        for id_barang, barang in data_barang.items():
            print("{:<10} {:<15} {:<15} {:<15} Rp.{:<12} {:<15} {:<10}".format(id_barang, barang["namaBarang"], barang["kategoriHewan"], barang["merk"], barang["harga"], barang["diskon"], barang["stok"]))

        print('\n[1]. Masukkan Kode Barang')
        print("\n[2]. Kembali")
        
        pilihan = input("\nPilih opsi (1/2): ")

        if pilihan == "1":
            kode_barang_hapus = input("\nMasukkan kode barang yang ingin dihapus: ").upper()
            
            if kode_barang_hapus in data_barang:
                print("\nInformasi barang yang akan dihapus:")
                print("Kode Barang:", kode_barang_hapus)
                print("Nama Barang:", data_barang[kode_barang_hapus]["namaBarang"])
                print("Kategori Hewan:", data_barang[kode_barang_hapus]["kategoriHewan"])
                print("Merk:", data_barang[kode_barang_hapus]["merk"])
                print("Harga:", data_barang[kode_barang_hapus]["harga"])
                print("Diskon:", data_barang[kode_barang_hapus]["diskon"])
                print("Stok:", data_barang[kode_barang_hapus]["stok"])
                
                konfirmasi = input(f"\nApakah Anda yakin ingin menghapus barang dengan kode {kode_barang_hapus}? (Y/N): ")
                if konfirmasi.lower() == 'y':
                    del data_barang[kode_barang_hapus]
                    print("\nItem dengan kode", kode_barang_hapus, "telah dihapus.")
                    admin()
                    return
                elif konfirmasi.lower() == 'n':
                    print("\nPenghapusan dibatalkan.")
                else:
                    print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")
            else:
                print("\nKode barang tidak ditemukan.")
        elif pilihan == "2":
            admin()
            return
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

def admin():
    while True:
        print("\nSelamat Datang Admin Petshop Umam :")
        print('\n[1]. Cek Item')
        print("\n[2]. Tambah Item")
        print("\n[3]. Edit Item")
        print("\n[4]. Hapus Item")
        print('\n[5]. Logout')

        pilihan = input("\nPilih opsi (1/2/3/4/5): ")

        if pilihan == "1":
            tampilAdmin()
            break
        elif pilihan == "2":
            tambahItem()
            break
        elif pilihan == '3':
            editItem()
            break
        elif pilihan == '4':
            hapus()
            break
        elif pilihan == "5":
            menuUtama()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
        

def adminLogin():
    while True:
        print("\nSelamat Datang Admin Petshop Umam :")
        print("\n[1]. Masukkan Username")
        print("\n[2]. Kembali")

        pilihan = input("\nPilih opsi (1/2): ")

        daftarAdmin = ['umam', 'admin', 'adminkecil']

        if pilihan == "1":
            username = input('\nMasukkan Username (Case-Sensitive): ')

            if username in daftarAdmin: 
                admin()
                break
            else:
                print('\nUsername Salah!')
                time.sleep(1)
        elif pilihan == '2':
            menuUtama()
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")



def menuUtama():
    while True:
        print("\nSelamat Datang di Petshop Umam :")
        print("\n[1]. Pelanggan")
        print("\n[2]. Admin")
        print("\n[3]. Keluar")

        pilihan = input("\nPilih opsi (1/2/3): ")

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
            print("\nPilihan tidak valid. Silakan pilih opsi yang benar.")

print('==========Petshop Umam==========')
menuUtama()
