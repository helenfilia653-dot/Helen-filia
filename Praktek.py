#Program Target Mahasiswa

nama = input("Nama : ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar dalam sistem!")

print("nama mahasiswa :" , nama)
print("target nilai :" , target)

percobaan = 0
maks_percobaan = 3
lulus = False

percobaan =+ 1
nilai = int(input(f"Masukkan nilai {percobaan} :"))

if nilai >= target :
    lulus = True

print ("-" * 30)

if lulus :
    print (f"output yang diharapkan:\n{nama}berhasil lulus setelah{percobaan} kali percobaan")

else :  
    print(f"output yang di harapkan:\n{nama}tidak lulus setelah{maks_percobaan} kali percobaan")