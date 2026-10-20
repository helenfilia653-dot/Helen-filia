Nilai_Tugas =int(input("masukkan nilai Tugas:"))
Uts = int(input("masukkan nilai UTS:"))
Uas = int(input("masukkan nilai UAS:"))
Kehadiran_Mahasiswa = int(input("masukkan nilai kehadiran:"))
nilai_akhir = (20 / 100 * Nilai_Tugas) + (30 / 100 * Uts) + (50 / 100 * Uas)
print("======HASIL======")
print("Nilai akhir =", nilai_akhir)
print(Kehadiran_Mahasiswa,"%")
if nilai_akhir >= 85 and Kehadiran_Mahasiswa >= 90 and nilai_akhir % 2 == 0:
    print( "Status : LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and Kehadiran_Mahasiswa >= 80:
    print("Status : LULUS")
else:
    print("Status : TIDAK LULUS")