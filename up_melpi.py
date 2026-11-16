# tugas algoritma - Melpi Aura

print("PROGRAM PENILAIAN MAHASISWA")

banyak = int(input("Berapa mahasiswa yang mau diinput? "))

lulus = 0
tidak_lulus = 0

i = 1
while i <= banyak:
    print()
    print("Mahasiswa ke", i)
    nama = input("Nama : ")
    nilai = int(input("Nilai : "))

    if nilai >= 85:
        hasil = "A"
        ket = "Sangat Baik"
    elif nilai >= 75:
        hasil = "B"
        ket = "Baik"
    elif nilai >= 60:
        hasil = "C"
        ket = "Cukup"
    else:
        hasil = "D"
        ket = "Tidak Lulus"

    print("Nama :", nama)
    print("Nilai :", nilai)
    print("Dapat :", hasil, "-", ket)

    if nilai >= 60:
        lulus = lulus + 1
    else:
        tidak_lulus = tidak_lulus + 1

    i = i + 1

print()
print("Total yang lulus :", lulus)
print("Total yang tidak lulus :", tidak_lulus)
print("Selesai")