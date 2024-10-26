class Order:
    def __init__(self, ID=0, nama="", details=""):
        self._ID = ID
        self.nama = nama
        self.details = details

    def displayOrder(self):
        print(f"Order ID: {self._ID}")
        print(f"Order Name: {self.nama}")
        print(f"Order Details: {self.details}")

    def delateOrder(self):
        print(f"Order {self._ID} berhasil dihapus")


class Delivery:
    def __init__(self, id=0, nama="", information="", date="", address=""):
        self._id = id
        self.nama = nama
        self.information = information
        self.date = date
        self.address = address

    def processDelivery(self):
        pass

    def displayDelivery(self):
        print(f"Delivery ID: {self._id}")
        print(f"Delivery Name: {self.nama}")
        print(f"Delivery Information: {self.information}")
        print(f"Delivery Date: {self.date}")
        print(f"Delivery Address: {self.address}")

    def deleteDelivery(self):
        print(f"Delivery {self._id} berhasil dihapus")


orders = []
deliveries = []

while True:
    print("======= Menu =======")
    print("1. Add Order")
    print("2. Add Delivery")
    print("3. View Orders")
    print("4. View Deliveries")
    print("5. delete Order")
    print("6. delete Delivery")
    print("7. Exit")

    pilih = int(input("pilih broo: "))

    if pilih == 1:
        id = int(input("Masukkan ID: "))
        nama = input("Masukkan nama: ")
        details = input("Masukkan details: ")
        order = Order(id, nama, details)
        orders.append(order)
        print("Order Berhasil bro")

    elif pilih == 2:
        id = int(input("Masukan id bro: "))
        nama = input("masukan nama:")
        information = input("masukan informasi: ")
        date = input("masukan date: ")
        address = input("masukan alamat: ")
        delivery = Delivery(id, nama, information, date, address)
        deliveries.append(delivery)
        print("Delivery Beres cuy")

    elif pilih == 3:
        if not orders:
            print("Tidak ada orderan bro")
        else:
            for order in orders:
                order.displayOrder()

    elif pilih == 4:
        if not deliveries:
            print("Tidak ada delivery bro")
        else:
            for delivery in deliveries:
                delivery.displayDelivery()

    elif pilih == 5:
        if not orders:
            print("Tidak ada orderan")
        else:
            id = int(input("Masukkan ID order yang ingin dihapus: "))
            for order in orders:
                if order._ID == id:
                    order.delateOrder()
                    orders.remove(order)
                    break
            else:
                print("Order tidak ditemukan")

    elif pilih == 6:
        if not deliveries:
            print("Tidak ada delivery")
        else:
            id = int(input("Masukkan ID delivery yang ingin dihapus: "))
            for delivery in deliveries:
                if delivery._id == id:
                    delivery.deleteDelivery()
                    deliveries.remove(delivery)
                    break
            else:
                print("delivery tidak ditemukan")

    elif pilih == 7:
        break

    else:
        print("pilih yang bener broo")