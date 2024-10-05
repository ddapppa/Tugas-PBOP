

class Daftar_Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def display(self):
        print(f"{self.nama}  RP.{self.harga}")


Daftar_makanan = []
Daftar_minuman = []


while True:
    print("### DAFTAR MENU  ###")
    print("1. Daftar Menu Makanan")
    print("2. Daftar Menu Minuman")
    print("3. Tambah Manu")
    print("4. exit")

    pilih= int(input("pilih menu : "))

    if pilih == 1:
        print("### MENU MAKANAN ###")
        print("1. Nasi Goreng", "Rp. 15.000")
        print("2. Ayam Geprek", "Rp. 20.000")
        print("3. Mie Ayam", "Rp. 10.000") 
        for Daftar2 in Daftar_makanan:
            Daftar2.display()

    
    elif pilih == 2:
        print("### MENU MINUMAN ###")
        print("1. Es teh", "Rp. 5.000")
        print("2. Es jeruk", "Rp. 6.000")
        print("3. Kopi", "Rp. 5.000")
        for Daftar1 in Daftar_minuman:
            Daftar1.display()


        
    elif pilih == 3:
        if pilih == 3:
            print("### DAFTAR MENU  ###")
            print("1. Menu Makanan")
            print("2. Menu Minuman")
            print("3. Tambah Menu")
            print("4. exit")
            nama = input("Masukkan nama makanan/minuman: ")
            harga = int(input("Masukkan harga makanan/minuman: "))
            Daftar1 = Daftar_Menu(nama, harga)
            Daftar_minuman.append(Daftar1)
            Daftar2 = Daftar_Menu(nama, harga)
            Daftar_makanan.append(Daftar2)

    elif pilih == 4:
        break




