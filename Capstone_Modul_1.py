import datetime

# Daftar Buku Awal (menggunakan dictionary dengan ID buku sebagai key)
buku_dict = {
    1: {"judul": "To Kill a Mockingbird", "pengarang": "Harper Lee", "tahun_terbit": 1960, "stok": 3, "pinjam": 0},
    2: {"judul": "1984", "pengarang": "George Orwell", "tahun_terbit": 1949, "stok": 2, "pinjam": 0},
    3: {"judul": "The Catcher in the Rye", "pengarang": "J.D. Salinger", "tahun_terbit": 1951, "stok": 4, "pinjam": 0},
    4: {"judul": "Moby-Dick", "pengarang": "Herman Melville", "tahun_terbit": 1851, "stok": 5, "pinjam": 0},
    5: {"judul": "The Great Gatsby", "pengarang": "F. Scott Fitzgerald", "tahun_terbit": 1925, "stok": 3, "pinjam": 0}
}

# Riwayat Peminjaman Buku
riwayat_peminjaman = []

# Fungsi Create: Menambahkan Buku
def tambah_buku():
    print("\n--- Tambah Buku Baru ---")
    # Memungkinkan input ID buku manual
    while True:
        try:
            id_buku = input("Masukkan ID Buku (biarkan kosong untuk ID otomatis): ")
            if id_buku == "":  # Jika kosong, otomatis ID akan melanjutkan ID terakhir
                id_buku = max(buku_dict.keys()) + 1 if buku_dict else 1
                break
            id_buku = int(id_buku)
            if id_buku <= 0:
                print("ID Buku tidak boleh bernilai negatif atau nol. Silakan pilih ID yang valid.")
            elif id_buku in buku_dict:
                print(f"ID Buku {id_buku} sudah ada. Silakan pilih ID lain.")
            else:
                break  # ID valid dan tidak ada duplikasi
        except ValueError:
            print("Masukkan ID Buku yang valid (angka).")

    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan pengarang buku: ")

    # Menggunakan try-except untuk menangani input tahun terbit
    while True:
        try:
            tahun_terbit = int(input("Masukkan tahun terbit buku : "))
            if tahun_terbit > 2024:
                print("Tahun terbit tidak boleh lebih dari 2024. Silakan masukkan tahun yang valid.")
            elif tahun_terbit < 1 :
                print ("Tahun terbit tidak boleh kurang dari 1. Silahkan masukkan tahun yang valid")
            else:
                break  # Keluar dari loop jika input valid
        except ValueError:
            print("Tahun terbit harus berupa angka. Silakan coba lagi.")

    while True:
        try:
            stok = int(input("Masukkan jumlah stok buku: "))
            if stok <= 0:
                print("Jumlah stok harus lebih besar dari 0. Silakan coba lagi.")
            else:
                break  # Keluar dari loop jika input valid
        except ValueError:
            print("Jumlah stok harus berupa angka. Silakan coba lagi.")
    
    buku_dict[id_buku] = {
        "judul": judul,
        "pengarang": pengarang,
        "tahun_terbit": tahun_terbit,
        "stok": stok,
        "pinjam": 0  # Inisialisasi peminjaman buku sebagai 0
    }
    print(f"Buku '{judul}' berhasil ditambahkan dengan ID Buku {id_buku}!")


# Fungsi Menampilkan Semua Buku
def tampilkan_seluruh_buku():
    if len(buku_dict) == 0:
        print("Tidak ada buku di perpustakaan.")
    else:
        print("\n" + "Daftar Buku Perpustakaan Momo".center(50, "-"))
        print(f"{'ID Buku':<8} {'Judul Buku':<30} {'Pengarang':<20} {'Tahun Terbit':<15} {'Stok':<5} {'Pinjam':<5}")
        print("-" * 85)
        for id_buku, info in buku_dict.items():
            print(f"{id_buku:<8} {info['judul']:<30} {info['pengarang']:<20} {info['tahun_terbit']:<15} {info['stok']:<5} {info['pinjam']:<5}")

# Fungsi Hapus Buku
def hapus_buku():
    tampilkan_seluruh_buku()
    try:
        id_buku = int(input("\nMasukkan ID Buku yang ingin dihapus: "))
        if id_buku in buku_dict:
            # Menghapus buku dari dictionary
            del buku_dict[id_buku]
            print(f"Buku dengan ID {id_buku} telah berhasil dihapus.")
        else:
            print("ID Buku tidak ditemukan.")
    except ValueError:
        print("Masukkan ID Buku yang valid.")

# Fungsi Update Buku
def update_buku():
    tampilkan_seluruh_buku()
    try:
        id_buku = int(input("\nMasukkan ID Buku yang ingin diupdate: "))
        if id_buku in buku_dict:
            print("\nApa yang ingin Anda update?")
            print("1. Judul Buku")
            print("2. Pengarang Buku")
            print("3. Tahun Terbit Buku")
            print("4. Stok Buku")
            print("5. ID Buku")

            pilihan = input("Pilih nomor (1-5): ")

            if pilihan == '1':
                judul = input("Masukkan judul buku baru: ")
                buku_dict[id_buku]['judul'] = judul
            elif pilihan == '2':
                pengarang = input("Masukkan pengarang buku baru: ")
                buku_dict[id_buku]['pengarang'] = pengarang
            elif pilihan == '3':
                while True:
                    try:
                        tahun_terbit = int(input("Masukkan tahun terbit buku baru (tidak boleh lebih dari 2024): "))
                        if tahun_terbit > 2024:
                            print("Tahun terbit tidak boleh lebih dari 2024. Silakan masukkan tahun yang valid.")
                        elif tahun_terbit < 1:
                            print("Tahun terbit tidak boleh kurang dari 1. Silakan masukkan tahun yang valid.")
                        else:
                            buku_dict[id_buku]['tahun_terbit'] = tahun_terbit
                            break
                    except ValueError:
                        print("Tahun terbit harus berupa angka. Silakan coba lagi.")
            elif pilihan == '4':
                while True:
                    try:
                        stok = int(input("Masukkan jumlah stok buku baru: "))
                        if stok <= 0:
                            print("Jumlah stok harus lebih besar dari 0. Silakan coba lagi.")
                        else:
                            buku_dict[id_buku]['stok'] = stok
                            break
                    except ValueError:
                        print("Jumlah stok harus berupa angka. Silakan coba lagi.")
            elif pilihan == '5':
                # Update ID Buku
                while True:
                    try:
                        id_baru = int(input("Masukkan ID Buku yang baru: "))
                        if id_baru in buku_dict:
                            print(f"ID Buku {id_baru} sudah ada. Silakan pilih ID lain.")
                        else:
                            # Simpan buku dengan ID baru dan hapus ID lama
                            buku_dict[id_baru] = buku_dict.pop(id_buku)
                            print(f"ID Buku berhasil diupdate menjadi {id_baru}.")
                            break
                    except ValueError:
                        print("Masukkan ID Buku yang valid (angka).")

            else:
                print("Pilihan tidak valid.")
            
            print(f"Buku dengan ID {id_buku} berhasil diperbarui.")
        else:
            print("ID Buku tidak ditemukan.")
    except ValueError:
        print("Masukkan ID Buku yang valid.")

# Fungsi Riwayat Peminjaman
def riwayat_peminjaman_buku():
    if not riwayat_peminjaman:
        print("\nTidak ada riwayat peminjaman buku.")
    else:
        print("\n" + "Riwayat Peminjaman Buku".center(50, "-"))
        print(f"{'ID Buku':<8} {'Judul Buku':<30} {'Nama Anggota':<20} {'Tanggal Peminjaman':<20} {'Tanggal Pengembalian':<20}")
        print("-" * 110)
        for riwayat in riwayat_peminjaman:
            # Menampilkan 'Belum Dikembalikan' jika tanggal pengembalian adalah None
            tanggal_pengembalian = riwayat['tanggal_pengembalian'] if riwayat['tanggal_pengembalian'] else 'Belum Dikembalikan'
            print(f"{riwayat['id_buku']:<8} {riwayat['judul']:<30} {riwayat['nama_anggota']:<20} "
                  f"{riwayat['tanggal_peminjaman']:<20} {tanggal_pengembalian:<20}")

# Fungsi Pinjam Buku (Multi-book pinjam)
def pinjam_buku():
    tampilkan_seluruh_buku()
    buku_yang_dipinjam = []
    
    while True:
        try:
            id_buku = int(input("\nMasukkan ID Buku yang ingin dipinjam (atau ketik 0 untuk selesai): "))
            if id_buku == 0:
                break  # Jika input 0, keluar dari loop
            if id_buku not in buku_dict:
                print("ID Buku tidak ditemukan, coba lagi.")
                continue

            buku = buku_dict[id_buku]
            if buku['stok'] > 0:  # Memeriksa stok yang tersedia
                # Menambahkan ID buku ke dalam informasi buku yang dipinjam
                buku_yang_dipinjam.append({**buku, 'id_buku': id_buku})  # Menambahkan id_buku ke objek buku
                buku['stok'] -= 1  # Kurangi stok
                buku['pinjam'] += 1  # Tambah jumlah buku yang dipinjam
            else:
                print(f"Buku '{buku['judul']}' stoknya habis.")
        except ValueError:
            print("Masukkan ID Buku yang valid.")
    
    if buku_yang_dipinjam:
        # Input nama anggota setelah seluruh proses peminjaman buku selesai
        nama_anggota = input("Masukkan nama anggota yang meminjam: ")

        # Mencatat riwayat peminjaman untuk buku yang berhasil dipinjam
        tanggal_peminjaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for buku in buku_yang_dipinjam:
            riwayat_peminjaman.append({
                'id_buku': buku['id_buku'],  # Sekarang bisa mengakses id_buku
                'judul': buku['judul'],
                'nama_anggota': nama_anggota,
                'tanggal_peminjaman': tanggal_peminjaman,
                'tanggal_pengembalian': None  # Belum dikembalikan
            })

        print(f"{len(buku_yang_dipinjam)} buku berhasil dipinjam!")
    else:
        print("Tidak ada buku yang dipinjam.")

# Fungsi Kembalikan Buku
def kembalikan_buku():
    tampilkan_seluruh_buku()
    try:
        id_buku = int(input("\nMasukkan ID Buku yang ingin dikembalikan: "))
        if id_buku in buku_dict:
            buku = buku_dict[id_buku]
            if buku['pinjam'] > 0:  # Memeriksa apakah ada buku yang dipinjam
                buku['stok'] += 1  # Menambahkan stok buku
                buku['pinjam'] -= 1  # Mengurangi jumlah buku yang dipinjam

                # Mencatat tanggal pengembalian di riwayat
                for riwayat in riwayat_peminjaman:
                    if riwayat['id_buku'] == id_buku and riwayat['tanggal_pengembalian'] is None:
                        riwayat['tanggal_pengembalian'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break

                print(f"Buku '{buku['judul']}' berhasil dikembalikan.")
            else:
                print("Tidak ada buku yang sedang dipinjam.")
        else:
            print("ID Buku tidak ditemukan.")
    except ValueError:
        print("Masukkan ID Buku yang valid.")

# Menu Utama
def menu():
    while True:
        print("\n" + "- - - - - - - - - - Selamat Datang di Perpustakaan Momo - - - - - - - - - -" )
        print("1. Daftar Buku")
        print("2. Tambah Buku")
        print("3. Hapus Buku")
        print("4. Pinjam Buku")
        print("5. Update Buku")
        print("6. Kembalikan Buku")
        print("7. Riwayat Peminjaman")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == '1':
            tampilkan_seluruh_buku()
        elif pilihan == '2':
            tambah_buku()
        elif pilihan == '3':
            hapus_buku()
        elif pilihan == '4':
            pinjam_buku()
        elif pilihan == '5':
            update_buku()
        elif pilihan == '6':
            kembalikan_buku()
        elif pilihan == '7':
            riwayat_peminjaman_buku()
        elif pilihan == '8':
            print("Terima kasih telah menggunakan Perpustakaan Momo. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

# Menjalankan menu
menu()
