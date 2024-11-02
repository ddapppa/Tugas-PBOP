class Produk:
    def __init__(self, _kode_produk, nama_produk, jenis_produk, harga):
        self._kode_produk = _kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def info(self):
        return f"{self.jenis_produk} - Nama: {self.nama_produk}, Harga: {self.harga}"


class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, "Snack", harga)


class Makanan(Produk):
    def __init__(self, kode_produk, __nama_makanan, __harga):
        super().__init__(kode_produk, __nama_makanan, "Makanan", __harga)


class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, "Minuman", harga)


class Pegawai:
    def __init__(self, _nik, nama, alamat):
        self._nik = _nik
        self.nama = nama
        self.alamat = alamat

    def info(self):
        return f"Nama: {self.nama}, Alamat: {self.alamat}"


class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi=[]):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi

    def tambah_transaksi(self, detail):
        self.detail_transaksi.append(detail)

    def display(self):
        print(f"No Transaksi: {self.no_transaksi}")
        for detail in self.detail_transaksi:
            print(detail.info())


class MenuProduk:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def hapus_produk(self, produk):
        self.daftar_produk.remove(produk)

    def display(self):
        if not self.daftar_produk:
            print("Daftar produk kosong.")
        else:
            print("Daftar Produk:")
            for produk in self.daftar_produk:
                print(produk.info())

class MenuPegawai:
    def __init__(self):
        self.daftar_pegawai = []  

    def tambah_pegawai(self, pegawai):
        self.daftar_pegawai.append(pegawai)

    def hapus_pegawai(self, pegawai):
        self.daftar_pegawai.remove(pegawai)

    def display(self):
        if not self.daftar_pegawai:
            print("Daftar pegawai kosong.")
        else:
            for pegawai in self.daftar_pegawai:
                print(pegawai.info())

class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi 

    def tambah_transaksi(self, detail_transaksi):
        self.detail_transaksi.append(detail_transaksi)

    def display(self):
        print(f"No Transaksi: {self.no_transaksi}")
        for detail in self.detail_transaksi:
            detail.display()



class Struk:
    def __init__(self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga

    def info(self):
        return (f"No Transaksi: {self.no_transaksi}, Nama Pegawai: {self.nama_pegawai}, "
                f"Nama Produk: {self.nama_produk}, Jumlah Produk: {self.jumlah_produk}, "
                f"Total Harga: {self.total_harga}")



def main():
    menu_produk = MenuProduk()
    menu_pegawai = MenuPegawai()

    menu_produk.tambah_produk(Snack("001", "Keripik Singkong", 5000))
    menu_produk.tambah_produk(Makanan("002", "Nasi Goreng", 15000))
    menu_produk.tambah_produk(Minuman("003", "Es Teh", 5000))


    menu_pegawai.tambah_pegawai(Pegawai("123", "Yori", "Jl. Kelapa Dua"))
    menu_pegawai.tambah_pegawai(Pegawai("456", "Arya", "Jl. Dayung"))
    menu_pegawai.tambah_pegawai(Pegawai("789", "Alief", "Jl. Bsd"))

    while True:
        print("\nMenu Utama")
        print("1. Produk")
        print("2. Pegawai")
        print("3. Keluar")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            sub_menu_produk(menu_produk)
        elif pilihan == "2":
            sub_menu_pegawai(menu_pegawai)
        elif pilihan == "3":
            break
        else:
            print("Menu tidak tersedia")


def sub_menu_produk(menu_produk):
    while True:
        print("\nMenu Produk")
        print("1. Tampilkan Semua Produk")
        print("2. Tambah Produk")
        print("3. Hapus Produk")
        print("4. Kembali")
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            menu_produk.display()
        elif pilihan == "2":
            nama_produk = input("Masukkan Nama Produk: ")
            jenis_produk = input("Masukkan Jenis Produk (Snack/Makanan/Minuman): ")
            harga = int(input("Masukkan Harga Produk: "))
            kode_produk = input("Masukkan Kode Produk: ")

            if jenis_produk.lower() == "snack":
                produk = Snack(kode_produk, nama_produk, harga)
            elif jenis_produk.lower() == "makanan":
                produk = Makanan(kode_produk, nama_produk, harga)
            elif jenis_produk.lower() == "minuman":
                produk = Minuman(kode_produk, nama_produk, harga)
            else:
                print("Jenis produk tidak valid.")
                continue

            menu_produk.tambah_produk(produk)
            print(f"{jenis_produk} berhasil ditambahkan.")
        elif pilihan == "3":
            nama_produk = input("Masukkan Nama Produk yang akan dihapus: ")
            produk_dihapus = None
            for produk in menu_produk.daftar_produk:
                if produk.nama_produk == nama_produk:
                    produk_dihapus = produk
                    break

            if produk_dihapus:
                menu_produk.hapus_produk(produk_dihapus)
                print(f"{nama_produk} berhasil dihapus.")
            else:
                print("Produk tidak ditemukan.")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak tersedia.")

def sub_menu_pegawai(menu_pegawai):
    while True:
        print("\nMenu Pegawai")
        print("1. Tampilkan Semua Pegawai")
        print("2. Tambah Pegawai")
        print("3. Hapus Pegawai")
        print("4. Kembali")

        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            menu_pegawai.display()

        elif pilihan == "2":
            nik = input("Masukkan NIK Pegawai: ")
            nama_pegawai = input("Masukkan Nama Pegawai: ")
            alamat = input("Masukkan Alamat Pegawai: ")
            pegawai_baru = Pegawai(nik, nama_pegawai, alamat)
            menu_pegawai.tambah_pegawai(pegawai_baru)
            print(f"Pegawai {nama_pegawai} berhasil ditambahkan.")

        elif pilihan == "3":
            nama_pegawai = input("Masukkan Nama Pegawai yang akan dihapus: ")
            pegawai_dihapus = None
            for pegawai in menu_pegawai.daftar_pegawai:
                if pegawai.nama == nama_pegawai:
                    pegawai_dihapus = pegawai
                    break


            if pegawai_dihapus:
                menu_pegawai.hapus_pegawai(pegawai_dihapus)
                print(f"Pegawai {nama_pegawai} berhasil dihapus.")
            else:
                print("Pegawai tidak ditemukan.")
                
        elif pilihan == "4":
            break
    
        else:
            print("Pilihan tidak tersedia.")



if __name__ == "__main__":
    main()
