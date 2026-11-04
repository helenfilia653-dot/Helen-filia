jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

total_nilai = 0

for i in range(1, jumlah_mahasiswa + 1):
    nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
    total_nilai += nilai

rata_rata = total_nilai / jumlah_mahasiswa

print(f"Nilai rata - rata : {rata_rata}")

print("======HASIL======")