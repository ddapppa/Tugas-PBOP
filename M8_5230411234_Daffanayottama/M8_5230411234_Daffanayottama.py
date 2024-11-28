import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import openpyxl 

class AppKehadiran:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pencatatan Kehadiran Siswa")
        self.root.geometry("900x700")
        self.siswa = []  # Daftar siswa
        self.create_widgets()

    def create_widgets(self):
        # Label Judul        
        title_label = tk.Label(self.root, text="Pencatatan Kehadiran Siswa", font=("Arial", 18, 'bold'))
        title_label.pack(pady=10)

        # Pilih Tanggal
        self.tanggal_label = tk.Label(self.root, text="Tanggal: ")
        self.tanggal_label.pack()
        self.tanggal_entry = tk.Entry(self.root, width=25)
        self.tanggal_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.tanggal_entry.pack(pady=5)

        # Pilih Kelas
        self.kelas_label = tk.Label(self.root, text="Kelas: ")
        self.kelas_label.pack()
        self.kelas_entry = tk.Entry(self.root, width=25)
        self.kelas_entry.pack(pady=5)

        # Nama Siswa dan Status Kehadiran
        self.nama_label = tk.Label(self.root, text="Nama Siswa: ")
        self.nama_label.pack()
        self.nama_entry = tk.Entry(self.root, width=25)
        self.nama_entry.pack(pady=5)

        self.status_label = tk.Label(self.root, text="Status Kehadiran: ")
        self.status_label.pack()
        self.status_var = tk.StringVar(value="Hadir")
        self.status_menu = ttk.Combobox(self.root, textvariable=self.status_var, values=("Hadir", "Tidak Hadir", "Izin", "Sakit"), state="readonly", width=20)
        self.status_menu.pack(pady=5)

        # Button untuk Menambahkan Kehadiran
        self.add_button = tk.Button(self.root, text="Tambah Kehadiran", command=self.add_kehadiran)
        self.add_button.pack(pady=10)

        # Daftar Kehadiran
        self.list_label = tk.Label(self.root, text="Daftar Kehadiran: ")
        self.list_label.pack(pady=10)

        self.treeview = ttk.Treeview(self.root, columns=("Tanggal", "Kelas", "Nama", "Status"), show="headings")
        self.treeview.heading("Tanggal", text="Tanggal")
        self.treeview.heading("Kelas", text="Kelas")
        self.treeview.heading("Nama", text="Nama")
        self.treeview.heading("Status", text="Status")
        self.treeview.pack(pady=10)

        # Button Clear
        self.clear_button = tk.Button(self.root, text="Clear Data", command=self.clear_data)
        self.clear_button.pack(pady=5)

        # Button Export
        self.export_button = tk.Button(self.root, text="Export to Excel", command=self.export_to_excel)
        self.export_button.pack(pady=5)

    def add_kehadiran(self):
        # Ambil data dari form
        tanggal = self.tanggal_entry.get()
        kelas = self.kelas_entry.get()
        nama = self.nama_entry.get()
        status = self.status_var.get()

        # Validasi input
        if not nama or not kelas:
            messagebox.showerror("Error", "Nama dan Kelas harus diisi!")
            return

        # Tambahkan data ke daftar
        self.treeview.insert("", "end", values=(tanggal, kelas, nama, status))

        # Kosongkan input setelah tambah
        self.nama_entry.delete(0, 'end')

    def clear_data(self):
        # Menghapus semua data dari treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def export_to_excel(self):
        # Membuat workbook baru
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Kehadiran Siswa"

        # Header
        headers = ["Tanggal", "Kelas", "Nama", "Status"]
        sheet.append(headers)

        # Data
        for item in self.treeview.get_children():
            row_data = self.treeview.item(item, "values")
            sheet.append(row_data)

        # Simpan file
        filename = f"Kehadiran_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        try:
            workbook.save(filename)
            messagebox.showinfo("Sukses", f"Data berhasil disimpan ke file: {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppKehadiran(root)
    root.mainloop()
