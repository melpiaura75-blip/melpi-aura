nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(input("Masukkan persentase kehadiran (%): "))

nilai_akhir = (20 * nilai_tugas / 100) + (30 * nilai_uts / 100) + (50 * nilai_uas / 100)

print("Nilai akhir:", round(nilai_akhir, 2))

if nilai_akhir >= 75 and kehadiran >= 80:
    if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
        print("Status: LULUS DENGAN PREDIKAT")
    else:
        print("Status: LULUS")
else:
    print("Status: BELUM LULUS")