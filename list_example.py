# list_example.py
# Contoh penggunaan LIST di Python

# Membuat list
buah = ["apel", "mangga", "jeruk", "pisang"]

# Menampilkan seluruh isi list
print("Daftar buah:", buah)

# Mengakses elemen list
print("Buah pertama:", buah[0])

# Menambahkan elemen baru
buah.append("melon")
print("Setelah ditambah melon:", buah)

# Menghapus elemen
buah.remove("jeruk")
print("Setelah jeruk dihapus:", buah)

# Mengurutkan list
buah.sort()
print("Setelah diurutkan:", buah)

# Menampilkan panjang list
print("Jumlah buah:", len(buah))
