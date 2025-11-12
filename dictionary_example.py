# dictionary_example.py
# Contoh penggunaan DICTIONARY di Python

# Membuat dictionary
mahasiswa = {
    "nama": "Wildan Krisyanto",
    "nim": "2504030092",
    "prodi": "Teknik Informatika"
}

# Menampilkan isi dictionary
print("Data Mahasiswa:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Mengakses nilai berdasarkan key
print("Nama:", mahasiswa["nama"])

# Menambah data baru
mahasiswa["angkatan"] = 2025
print("Setelah ditambah angkatan:", mahasiswa)

# Menghapus data
del mahasiswa["prodi"]
print("Setelah prodi dihapus:", mahasiswa)
