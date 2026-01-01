import os
from datetime import datetime

print("\n" + "="*60)
print("SELAMAT DATANG DI TOKO BUKU ARIF \nJl. Cinta Konoha No.53, Mojoroto, Kota Kediri\nTelp: 081234567890")
print("="*60 + "\n")
print("Selamat bekerja dan jangan lupa senyum dan berdoa!")

def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

stok_barang = [
    {'judul': 'Harry Potter', 'penerbit': 'Bloomsbury', 'tahun': 1997, 'stok': 10, 'harga_barang': 50000, 'kategori': 'cerita'},
    {'judul': 'Kancil Mencuri Timun', 'penerbit': 'Gramedia', 'tahun': 2015, 'stok': 8, 'harga_barang': 30000, 'kategori': 'cerita'},
    {'judul': 'The Great Gatsby', 'penerbit': 'Scribner', 'tahun': 1925, 'stok': 5, 'harga_barang': 45000, 'kategori': 'cerita'},
    {'judul': 'Matematika Dasar', 'penerbit': 'Erlangga', 'tahun': 2020, 'stok': 20, 'harga_barang': 60000, 'kategori': 'pelajaran'},
    {'judul': 'Fisika untuk SMA', 'penerbit': 'Yudhistira', 'tahun': 2021, 'stok': 15, 'harga_barang': 55000, 'kategori': 'pelajaran'},
    {'judul': 'Kimia Organik', 'penerbit': 'Andi', 'tahun': 2019, 'stok': 12, 'harga_barang': 70000, 'kategori': 'pelajaran'},
    {'judul': 'Buku Tulis', 'penerbit': 'Sinar Dunia', 'tahun': 2023, 'stok': 50, 'harga_barang': 10000, 'kategori': 'tulis'},
    {'judul': 'Buku Gambar', 'penerbit': 'Vison', 'tahun': 2022, 'stok': 100, 'harga_barang': 5000, 'kategori': 'tulis'},
    {'judul': 'Pensil 2B', 'penerbit': 'Faber-Castell', 'tahun': 2024, 'stok': 200, 'harga_barang': 3000, 'kategori': 'tulis'},
    {'judul': 'Penghapus', 'penerbit': 'Staedtler', 'tahun': 2024, 'stok': 150, 'harga_barang': 2000, 'kategori': 'tulis'},
    {'judul': 'Pulpen Biru', 'penerbit': 'Pilot', 'tahun': 2023, 'stok': 180, 'harga_barang': 4000, 'kategori': 'tulis'},
]

riwayat_transaksi = []

def list_stok():
    print("\nDaftar Stok Barang:")
    kategori_buku = {
        "cerita": "Buku Cerita",
        "pelajaran": "Buku Pelajaran",
        "tulis": "Alat Tulis",
    }
    for kategori, nama in kategori_buku.items():
        print(f"\n{nama}:")
        for item in stok_barang:
            if item['kategori'] == kategori:
                print(
                    f"Judul: {item['judul']}, "
                    f"Penerbit: {item['penerbit']}, "
                    f"Tahun: {item['tahun']}, "
                    f"Stok: {item['stok']}, "
                    f"Harga: {format_rupiah(item['harga_barang'])}"
                )

def add_item():
    judul = input("Judul: ")
    penerbit = input("Penerbit: ")
    tahun = int(input("Tahun Terbit: "))
    stok = int(input("Stok: "))
    harga_barang = int(input("Harga: "))
    kategori = input("Kategori (cerita/pelajaran/tulis): ")

    stok_barang.append({
        'judul': judul,
        'penerbit': penerbit,
        'tahun': tahun,
        'stok': stok,
        'harga_barang': harga_barang,
        'kategori': kategori
    })

    print("Barang ditambahkan!")

def edit_item():
    judul = input("Judul barang yang ingin diperbarui: ")

    for item in stok_barang:
        if item['judul'].lower() == judul.lower():
            print("\nTekan ENTER jika tidak ingin mengubah data.")

            penerbit_baru = input(f"Penerbit baru ({item['penerbit']}): ")
            if penerbit_baru != "":
                item['penerbit'] = penerbit_baru

            tahun_baru = input(f"Tahun Terbit baru ({item['tahun']}): ")
            if tahun_baru != "":
                item['tahun'] = int(tahun_baru)

            stok_baru = input(f"Stok baru ({item['stok']}): ")
            if stok_baru != "":
                item['stok'] = int(stok_baru)

            harga_baru = input(f"Harga baru ({item['harga_barang']}): ")
            if harga_baru != "":
                item['harga_barang'] = int(harga_baru)

            print("Data barang sudah diperbarui!")
            return

    print("Barang tidak ditemukan!")

def hapus_barang():
    judul = input("Judul barang yang ingin dihapus: ")
    for item in stok_barang:
        if item['judul'].lower() == judul.lower():
            stok_barang.remove(item)
            print("Barang dihapus!")
            return
    print("Barang tidak ditemukan!")

def simpan_riwayat(nama_pegawai, cart, total, uang_bayar, kembali):
    riwayat_transaksi.append({
        "tanggal": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "pegawai": nama_pegawai,
        "items": cart,
        "total": total,
        "uang_bayar": uang_bayar,
        "kembali": kembali
    })

def lihat_riwayat():
    print("\n=== Riwayat Transaksi ===")
    if len(riwayat_transaksi) == 0:
        print("Belum ada transaksi.")
        return

    for i, trx in enumerate(riwayat_transaksi, 1):
        print(f"\nTransaksi {i}")
        print(f"Tanggal : {trx['tanggal']}")
        print(f"Pegawai : {trx['pegawai']}")
        print("Daftar Barang:")
        for item in trx['items']:
            print(f"- {item['judul']} x {item['qty']} = {format_rupiah(item['subtotal'])}")
        print(f"Total Belanja : {format_rupiah(trx['total'])}")
        print(f"Uang Bayar    : {format_rupiah(trx['uang_bayar'])}")
        print(f"Kembalian     : {format_rupiah(trx['kembali'])}")

def checkout(nama_pegawai):
    cart = []
    total = 0
    book_count = 0

    while True:
        judul = input("Masukkan judul buku (atau 'selesai' untuk checkout): ")
        if judul.lower() == 'selesai':
            break

        qty = int(input("Jumlah: "))
        found = False

        for item in stok_barang:
            if item['judul'].lower() == judul.lower():
                found = True

                if item['stok'] >= qty:
                    item['stok'] -= qty
                    subtotal = item['harga_barang'] * qty
                    discount = 0

                    if item['kategori'] in ['cerita', 'pelajaran']:
                        discount += subtotal * 0.10
                        book_count += qty

                    cart.append({
                        'judul': item['judul'],
                        'harga_barang': item['harga_barang'],
                        'qty': qty,
                        'subtotal': subtotal,
                        'discount': discount
                    })
                else:
                    print("Stok tidak cukup!")
                break

        if not found:
            print("Barang tidak ditemukan!")

    subtotal_all = sum(item['subtotal'] for item in cart)
    diskon_item = sum(item['discount'] for item in cart)

    potongan_qty = 0
    if book_count > 0:
        if book_count <= 5:
            potongan_qty = 10000
        elif book_count <= 7:
            potongan_qty = 20000
        else:
            potongan_qty = 30000

    temp_total = subtotal_all - diskon_item - potongan_qty

    member = input("Apakah Anda memiliki member? (ya/tidak): ").lower() == 'ya'
    diskon_member = temp_total * 0.1 if member else 0

    total_diskon = diskon_item + potongan_qty + diskon_member
    total_belanja = subtotal_all - total_diskon

    print(f"\nTotal Belanja: {format_rupiah(total_belanja)}")

    uang_bayar = int(input("Uang pembayaran: "))
    kembali = uang_bayar - total_belanja

    if kembali < 0:
        print("Uang tidak cukup!")
        return

    print("\n" + "="*60)
    print("TOKO BUKU ARIF")
    print("Jl. Cinta Konoha No.53, Mojoroto, Kota Kediri")
    print("Telp: 081234567890")
    print("="*60)
    print(f"Tanggal: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Pegawai: {nama_pegawai}")
    print("-"*60)
    print("Item".ljust(20) + "Qty".rjust(5) + "Harga".rjust(15) + "Subtotal".rjust(15))
    print("-"*60)

    for item in cart:
        print(f"{item['judul'][:18].ljust(20)} "
              f"{str(item['qty']).rjust(5)} "
              f"{format_rupiah(item['harga_barang']).rjust(15)} "
              f"{format_rupiah(item['subtotal']).rjust(15)}")

    print("-"*60)
    print(f"{'Subtotal:':<30} {format_rupiah(subtotal_all):>25}")

    if potongan_qty > 0:
        print(f"{'Potongan Qty:':<30} -{format_rupiah(potongan_qty):>24}")

    if diskon_member > 0:
        print(f"{'Diskon Member 10%:':<30} -{format_rupiah(int(diskon_member)):>24}")

    print(f"{'Uang Pembayaran:':<30} {format_rupiah(uang_bayar):>25}")
    print(f"{'Kembali:':<30} {format_rupiah(kembali):>25}")
    print("="*60)
    print("Terima Kasih atas Kunjungan Anda!")
    print("Barang yang sudah dibeli tidak dapat dikembalikan!")
    print("="*60)

    simpan_riwayat(nama_pegawai, cart, total_belanja, uang_bayar, kembali)

def main():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == 'admin' and password == '123':
            nama_pegawai = input("Masukkan nama lengkap karyawan: ")
            break
        else:
            print("Pastikan Username dan Password Benar!")

    while True:
        print("\n" + "="*40)
        print("\nMenu:")
        print("1. Lihat Stok")
        print("2. Tambah Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Checkout")
        print("6. Riwayat Transaksi")
        print("7. Keluar")
        print("="*40)
        print()
        choice = input("Pilih menu: ")

        if choice == '1':
            list_stok()
        elif choice == '2':
            add_item()
        elif choice == '3':
            edit_item()
        elif choice == '4':
            hapus_barang()
        elif choice == '5':
            checkout(nama_pegawai)
        elif choice == '6':
            lihat_riwayat()
        elif choice == '7':
            print("Terimakasih atas kerja keras hari ini\nSampai jumpa lagi!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()