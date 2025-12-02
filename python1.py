# a. Membuat variabel
nilai_int = 10
nilai_float = 3.14
nilai_str = "Zahra"
nilai_list = [1, 2, 3]

# b. Menampilkan tipe data
print(type(nilai_int))
print(type(nilai_float))
print(type(nilai_str))
print(type(nilai_list))

# a. List belanja
belanja = ["beras", "minyak", "telur"]

# b. Tambah item gula dan kopi
belanja.append("gula")
belanja.append("kopi")

# c. Tampilkan semua item dengan perulangan
for item in belanja:
    print(item)

# a. Dictionary harga
harga = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

# b. Hitung total harga
total = sum(harga.values())
print("Total harga:", total)

import math

def hitung_lingkaran(r):
    luas = math.pi * r * r
    keliling = 2 * math.pi * r
    return luas, keliling

# contoh pemanggilan
luas, keliling = hitung_lingkaran(7)
print("Luas:", luas)
print("Keliling:", keliling)

usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")
