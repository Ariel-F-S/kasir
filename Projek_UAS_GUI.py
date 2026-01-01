import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

# ================= UTIL =================
def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

# ================= DATA =================
stok_barang = [
    {'judul': 'Harry Potter', 'penerbit': 'Bloomsbury', 'tahun': 1997, 'stok': 10, 'harga': 50000, 'kategori': 'cerita'},
    {'judul': 'Kancil Mencuri Timun', 'penerbit': 'Gramedia', 'tahun': 2015, 'stok': 8, 'harga': 30000, 'kategori': 'cerita'},
    {'judul': 'The Great Gatsby', 'penerbit': 'Scribner', 'tahun': 1925, 'stok': 5, 'harga': 45000, 'kategori': 'cerita'},
    {'judul': 'Matematika Dasar', 'penerbit': 'Erlangga', 'tahun': 2020, 'stok': 20, 'harga': 60000, 'kategori': 'pelajaran'},
    {'judul': 'Fisika untuk SMA', 'penerbit': 'Yudhistira', 'tahun': 2021, 'stok': 15, 'harga': 55000, 'kategori': 'pelajaran'},
    {'judul': 'Pulpen Biru', 'penerbit': 'Pilot', 'tahun': 2023, 'stok': 180, 'harga': 4000, 'kategori': 'tulis'},
]

riwayat_transaksi = []

# ================= APP =================
class TokoBukuGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TOKO BUKU ARIF - SISTEM KASIR")
        self.geometry("1200x650")
        self.resizable(False, False)

        self.nama_pegawai = ""
        self.cart = []

        self.login_screen()

    # ================= LOGIN =================
    def login_screen(self):
        self.clear()
        frame = tk.Frame(self, padx=40, pady=30)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="TOKO BUKU ARIF", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(frame, text="Login Kasir").pack()

        self.user = tk.Entry(frame, width=30)
        self.passw = tk.Entry(frame, width=30, show="*")
        self.user.pack(pady=5)
        self.passw.pack(pady=5)

        tk.Label(frame, text="admin / 123", fg="gray").pack()

        tk.Button(frame, text="LOGIN", width=25, command=self.login).pack(pady=10)

    def login(self):
        if self.user.get() == "admin" and self.passw.get() == "123":
            self.nama_pegawai = simpledialog.askstring("Pegawai", "Masukkan nama pegawai:")
            if not self.nama_pegawai:
                return
            self.main_screen()
        else:
            messagebox.showerror("Error", "Username atau password salah")

    # ================= MAIN =================
    def main_screen(self):
        self.clear()

        sidebar = tk.Frame(self, bg="#2c3e50", width=200)
        sidebar.pack(side="left", fill="y")

        menu = [
            ("Stok Barang", self.show_stok),
            ("Tambah Barang", self.tambah_barang),
            ("Edit Barang", self.edit_barang),
            ("Hapus Barang", self.hapus_barang),
            ("Checkout", self.checkout_screen),
            ("Riwayat", self.riwayat_screen),
            ("Keluar", self.destroy),
        ]

        for text, cmd in menu:
            tk.Button(sidebar, text=text, width=20, pady=10,
                      bg="#2c3e50", fg="white", command=cmd).pack(pady=2)

        self.content = tk.Frame(self)
        self.content.pack(side="right", fill="both", expand=True)

        self.show_stok()

    # ================= STOK =================
    def show_stok(self):
        self.clear_content()

        tk.Label(self.content, text="DATA STOK BARANG",
                 font=("Arial", 16, "bold")).pack(pady=10)

        cols = ("Judul", "Penerbit", "Tahun", "Stok", "Harga", "Kategori")
        self.tree = ttk.Treeview(self.content, columns=cols, show="headings", height=18)

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        for item in stok_barang:
            self.tree.insert("", "end", values=(
                item['judul'], item['penerbit'], item['tahun'],
                item['stok'], format_rupiah(item['harga']), item['kategori']
            ))

        self.tree.pack(fill="x", padx=20)

    # ================= CRUD =================
    def tambah_barang(self):
        self.form_barang("Tambah Barang")

    def edit_barang(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Pilih", "Pilih barang dulu")
            return
        self.form_barang("Edit Barang", self.tree.item(selected)['values'])

    def form_barang(self, title, values=None):
        win = tk.Toplevel(self)
        win.title(title)
        win.geometry("400x450")

        labels = ["Judul", "Penerbit", "Tahun", "Stok", "Harga", "Kategori"]
        entries = []

        for i, lab in enumerate(labels):
            tk.Label(win, text=lab).pack()
            e = tk.Entry(win)
            e.pack()
            if values:
                e.insert(0, values[i])
            entries.append(e)

        def simpan():
            data = {
                'judul': entries[0].get(),
                'penerbit': entries[1].get(),
                'tahun': int(entries[2].get()),
                'stok': int(entries[3].get()),
                'harga': int(str(entries[4].get()).replace("Rp", "").replace(".", "")),
                'kategori': entries[5].get()
            }
            if values:
                for item in stok_barang:
                    if item['judul'] == values[0]:
                        item.update(data)
            else:
                stok_barang.append(data)

            self.show_stok()
            win.destroy()

        tk.Button(win, text="Simpan", command=simpan).pack(pady=10)

    def hapus_barang(self):
        selected = self.tree.focus()
        if not selected:
            return
        judul = self.tree.item(selected)['values'][0]
        for item in stok_barang:
            if item['judul'] == judul:
                stok_barang.remove(item)
                break
        self.show_stok()

    # ================= CHECKOUT =================
    def checkout_screen(self):
        self.clear_content()
        self.cart.clear()

        tk.Label(self.content, text="CHECKOUT",
                 font=("Arial", 16, "bold")).pack(pady=10)

        cols = ("Judul", "Kategori", "Harga", "Qty", "Subtotal")
        self.cart_tree = ttk.Treeview(self.content, columns=cols, show="headings", height=10)

        for c in cols:
            self.cart_tree.heading(c, text=c)
            self.cart_tree.column(c, anchor="center")

        self.cart_tree.pack(fill="x", padx=20)

        btn = tk.Frame(self.content)
        btn.pack(pady=10)

        tk.Button(btn, text="Tambah Item", command=self.add_cart).pack(side="left", padx=5)
        tk.Button(btn, text="Bayar", command=self.bayar).pack(side="left", padx=5)

    def add_cart(self):
        win = tk.Toplevel(self)
        win.title("Pilih Barang")
        win.geometry("700x400")

        cols = ("Judul", "Kategori", "Harga", "Stok")
        tree = ttk.Treeview(win, columns=cols, show="headings")

        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, anchor="center")

        for item in stok_barang:
            tree.insert("", "end", values=(
                item['judul'], item['kategori'],
                format_rupiah(item['harga']), item['stok']
            ))

        tree.pack(fill="both", expand=True)

        def pilih():
            selected = tree.focus()
            if not selected:
                return
            judul, kategori, _, _ = tree.item(selected)['values']
            qty = simpledialog.askinteger("Qty", "Jumlah beli:")
            for item in stok_barang:
                if item['judul'] == judul and item['stok'] >= qty:
                    item['stok'] -= qty
                    self.cart.append({
                        'judul': judul,
                        'kategori': kategori,
                        'harga': item['harga'],
                        'qty': qty,
                        'subtotal': qty * item['harga']
                    })
                    break
            self.refresh_cart()
            win.destroy()

        tk.Button(win, text="Tambah", command=pilih).pack(pady=5)

    def refresh_cart(self):
        for i in self.cart_tree.get_children():
            self.cart_tree.delete(i)
        for item in self.cart:
            self.cart_tree.insert("", "end", values=(
                item['judul'], item['kategori'],
                format_rupiah(item['harga']), item['qty'],
                format_rupiah(item['subtotal'])
            ))

    def bayar(self):
        subtotal_all = sum(i['subtotal'] for i in self.cart)

        diskon_item = sum(i['subtotal'] * 0.1 for i in self.cart
                          if i['kategori'] in ['cerita', 'pelajaran'])

        jumlah_buku = sum(i['qty'] for i in self.cart
                          if i['kategori'] in ['cerita', 'pelajaran'])

        potongan_qty = 10000 if jumlah_buku <= 5 else 20000 if jumlah_buku <= 7 else 30000

        member = messagebox.askyesno("Member", "Apakah customer member?")
        diskon_member = (subtotal_all - diskon_item - potongan_qty) * 0.1 if member else 0

        total = subtotal_all - diskon_item - potongan_qty - diskon_member

        uang_bayar = simpledialog.askinteger(
            "Pembayaran", f"Total: {format_rupiah(total)}\nUang bayar:"
        )
        if uang_bayar < total:
            messagebox.showerror("Error", "Uang tidak cukup")
            return

        kembali = uang_bayar - total

        riwayat_transaksi.append({
            "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "pegawai": self.nama_pegawai,
            "items": self.cart,
            "total": total,
            "uang_bayar": uang_bayar,
            "kembali": kembali
        })

        self.struk(subtotal_all, diskon_item, potongan_qty,
                   diskon_member, total, uang_bayar, kembali)

    # ================= STRUK (1:1 CLI) =================
    def struk(self, subtotal_all, diskon_item, potongan_qty,
              diskon_member, total_belanja, uang_bayar, kembali):

        win = tk.Toplevel(self)
        win.title("STRUK PEMBAYARAN")
        win.geometry("520x600")

        txt = tk.Text(win, font=("Courier New", 10))
        txt.pack(fill="both", expand=True)

        txt.insert("end", "="*60 + "\n")
        txt.insert("end", "TOKO BUKU ARIF\n")
        txt.insert("end", "Jl. Cinta, Kota Kediri\n")
        txt.insert("end", "Telp: 08123456789\n")
        txt.insert("end", "="*60 + "\n")

        txt.insert("end", f"Tanggal: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        txt.insert("end", f"Pegawai: {self.nama_pegawai}\n")
        txt.insert("end", "-"*60 + "\n")

        txt.insert("end",
            "Item".ljust(20) +
            "Qty".rjust(5) +
            "Harga".rjust(15) +
            "Subtotal".rjust(15) + "\n"
        )
        txt.insert("end", "-"*60 + "\n")

        for item in self.cart:
            txt.insert("end",
                item['judul'][:18].ljust(20) +
                str(item['qty']).rjust(5) +
                format_rupiah(item['harga']).rjust(15) +
                format_rupiah(item['subtotal']).rjust(15) + "\n"
            )

        txt.insert("end", "-"*60 + "\n")
        txt.insert("end", f"{'Subtotal:':<30} {format_rupiah(subtotal_all):>25}\n")
        txt.insert("end", f"{'Potongan Qty:':<30} -{format_rupiah(potongan_qty):>24}\n")
        txt.insert("end", f"{'Diskon Member 10%:':<30} -{format_rupiah(int(diskon_member)):>24}\n")
        txt.insert("end", f"{'Uang Pembayaran:':<30} {format_rupiah(uang_bayar):>25}\n")
        txt.insert("end", f"{'Kembali:':<30} {format_rupiah(kembali):>25}\n")
        txt.insert("end", "="*60 + "\n")
        txt.insert("end", "Terima Kasih atas Kunjungan Anda!\n")
        txt.insert("end", "Barang yang sudah dibeli tidak dapat dikembalikan!\n")
        txt.insert("end", "="*60 + "\n")

        txt.config(state="disabled")

    # ================= RIWAYAT =================
    def riwayat_screen(self):
        self.clear_content()
        txt = tk.Text(self.content)
        txt.pack(fill="both", expand=True)

        for i, r in enumerate(riwayat_transaksi, 1):
            txt.insert("end",
                f"{i}. {r['tanggal']} | {r['pegawai']} | {format_rupiah(r['total'])}\n"
            )

    # ================= UTIL =================
    def clear(self):
        for w in self.winfo_children():
            w.destroy()

    def clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()


# ================= RUN =================
if __name__ == "__main__":
    app = TokoBukuGUI()
    app.mainloop()
