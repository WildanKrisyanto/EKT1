# tuple_example.py
# Contoh penggunaan TUPLE di Python

# Membuat tuple
angka = (10, 20, 30, 40, 50)

# Menampilkan seluruh isi tuple
print("Isi tuple:", angka)

# Mengakses elemen tuple
print("Elemen pertama:", angka[0])
print("Elemen terakhir:", angka[-1])

# Menghitung jumlah elemen tertentu
print("Jumlah angka 20:", angka.count(20))

# Menampilkan panjang tuple
print("Panjang tuple:", len(angka))

# Tuple tidak bisa diubah (immutable)
# angka[0] = 99  <-- Ini akan error
