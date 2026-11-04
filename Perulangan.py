def sistem_penilaian():
    print("=== SISTEM PENILAIAN MAHASISWA ===")
    
    
    while True:
        try:
            jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
            if jumlah_mahasiswa > 0:
                break
            print("Jumlah mahasiswa harus lebih dari 0.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka bulat.")

    total_nilai = 0

  
    for i in range(1, jumlah_mahasiswa + 1):
        while True:
            try:
                nilai = float(input(f"Masukkan Nilai mahasiswa {i}: "))
                if 0 <= nilai <= 100:
                    total_nilai += nilai
                    break
                print("Nilai harus berada dalam rentang 0 sampai 100.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka yang benar.")

    
    rata_rata = total_nilai / jumlah_mahasiswa
    
    print("\n--- HASIL PENILAIAN ---")
    print(f"Nilai rata-rata : {rata_rata}")

if __name__ == "__main__":
    sistem_penilaian()