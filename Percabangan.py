#input
nilai = int(input("Masukkan Nilai:"))
#Proses
if nilai >= 80 and nilai <=100:
    print ("Anda Mendapatkan Nilai A")
elif nilai >=70 and nilai <=80:
    print("Anda Mendapatkan Nilai B")
elif nilai >=50 and nilai <=70:
    print("Anda Mendapatkan Nilai c")
elif nilai >=30 and nilai <=50:
    print("Anda Mendapatkan Nilai D")
elif nilai >=0 and nilai <=20:
    print("Anda Mendapatkan Nilai E")
else:
    print("Data Tidak Valid")

print("========Latihan========")

# input
nama_barang = input("Masukkan Nama Barang:")
harga_barang = int(input("Masukkan Harga Barang:"))

# proses
if nama_barang == "kulkas":
    diskon = 0.10 * harga_barang  # Diskon 10%
    jumlah_bayar = harga_barang - diskon
    print("Anda membeli Kulkas dengan diskon 10%")
elif nama_barang == "tv":
    diskon = 0.05 * harga_barang  # Diskon 5%
    jumlah_bayar = harga_barang - diskon
    print("Anda membeli TV dengan diskon 5%")
elif nama_barang == "radio":
    diskon = 0  # Tanpa diskon
    jumlah_bayar = harga_barang
    print("Anda membeli Radio tanpa diskon")
else:
    jumlah_bayar = harga_barang
    print("Nama barang tidak valid!")

# output
print("================================")
print("Jumlah Bayar = ", jumlah_bayar)
print("================================")