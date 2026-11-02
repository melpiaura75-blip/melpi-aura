#perulangan
# Program Sistem Penilaian Mahasiswa
jumlah_mhs = int(input("jumlah mahasiswa : "))

total_nilai = 0

for i in range(1, jumlah_mhs + 1):
    nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
    total_nilai += nilai
  
    if nilai >= 75:
        print(f"Mahasiswa {i} - Keterangan: Lulus")
    else:
        print(f"Mahasiswa {i} - Keterangan: Perbaikan")

rata_rata = total_nilai / jumlah_mhs

print(f"Nila rata - rata : {rata_rata}")