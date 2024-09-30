# Membuat input login sederhana dengan menggunakan logika perulangan agar user dapat login kembali jika gagal
while True:
    # Memberikan data pengguna
    nama = "Narendra Augusta Srianandha" 
    nim = 2409116010
    kelas = "A 24"
    # Menginput data pengguna
    print("======LOGIN======LOGIN======LOGIN======")
    print("Pastikan Nama, NIM, dan Kelas yang Anda Masukan Benar!")
    input_nama = input("Masukan nama anda: ")
    input_nim = int(input("Masukan NIM anda: "))
    input_kelas = input("Masukan Kelas anda: ")
    print("======LOGIN======LOGIN======LOGIN======")
    # Mengecek validitas data
    if input_nama == nama and input_nim == nim and input_kelas == kelas:
        print("Selamat",nama,"! Anda telah berhasil masuk!") # Mencetak kata ucapan apabila berhasil
        break # Keluar dari loop jika data valid
    else:
        print("\nLogin Gagal! Nama, NIM, atau Kelas yang anda masukan salah") # Cetak kegagalan dalam login
        opsi = input("Apakah anda ingin mencoba untuk masuk lagi? (ya/tidak): ")
        if opsi != 'ya': # Memberikan opsi pilihan ya atau tidak
            print("Program selesai, Selamat Tinggal /wave.") #  Cetak ucapan selamat tinggal
            exit()

# Menggunakan input untuk harga barang dan jumlah pembelian
while True:
    print("\nTentukan Harga Barang dan Jumlah Pembelian")
    harga_barang = int(input("Masukan harga barang: Rp. "))
    jumlah_pembelian = int(input("Masukan jumlah barang yang dibeli: "))

# Memberikan Rumus Total Harga dan Diskon
    total_harga = harga_barang * jumlah_pembelian
    syarat_diskon = 250000
    diskon = 0.25 * total_harga

# Membuat percabangan untuk menentukan apakah total harga barang lebih dari Rp. 250.000. Jika lebih, tambahkan diskon sebesar 25%. Sedangkan jika tidak mencapai lebih dari Rp.250.000, maka tidak mendapatkan diskon
    if total_harga > syarat_diskon:
        harga_akhir = total_harga - diskon
        print("\nSelamat Anda Mendapatkan Potongan Harga Sebesar 25%!")
        print(f"Total harga: Rp. {harga_akhir}") # Total dari penghitungan total harga dikali 25%
        print(f"Anda Berhasil Menghemat Sebanyak Rp. {diskon}!")
    else:
        print(f"Total harga: Rp. {total_harga}") # Hanya menampilkan total harga biasa tanpa potongan
        print("Program selesai, Selamat Tinggal /wave.")

# Menerapkan perulangan untuk memberikan pilihan apakah ingin menghitung total harga lagi atau keluar dari program
    print("\nApakah Anda Ingin Menghitung Lagi Total Harga?")
    opsi = input("ya/tidak: ")# Diberikan pilihan untuk perulangan dengan opsi ya atau tidak
    if opsi != 'ya':
        print("Program selesai, Selamat Tinggal /wave.")
        break
