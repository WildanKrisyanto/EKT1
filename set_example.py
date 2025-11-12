# set_example.py
# Contoh penggunaan SET di Python

# Membuat set
huruf = {"a", "b", "c", "d"}

# Menampilkan seluruh isi set
print("Isi set:", huruf)

# Menambahkan elemen baru
huruf.add("e")
print("Setelah ditambah e:", huruf)

# Menghapus elemen
huruf.remove("b")
print("Setelah b dihapus:", huruf)

# Operasi himpunan
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Irisan:", set1 & set2)
print("Gabungan:", set1 | set2)
print("Selisih:", set1 - set2)
