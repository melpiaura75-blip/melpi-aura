# input
nilai = int(input("Masukkan Nilai: "))
# proses 
if nilai >=80 and nilai<=100:
    print("Anda Mendapatkan Nilai A")
elif nilai >=70 and nilai <=80:
     print("Anda Mendapatkan Nilai B")
elif nilai >=50 and nilai <=70:
     print("Anda Mendapatkan Nilai C")     
elif nilai >=30 and nilai <=50:
     print("Anda Mendapatkan Nilai D")    
elif nilai >=0 and nilai <=20:
     print("Anda Mendapatkan NilaI E")
else:
     print("Data Tidak Valid")
print("=========LATIHAN=========")
#input
namabarang =input("Masukkan Nama Barang:")
hargabarang =int (input("Masukkan Harga Barang:"))
#proses
if namabarang=="kulkas":
     print (hargabarang - 0.10)
elif namabarang =="tv":
     print(hargabarang - 0.5)
elif namabarang=="radio":
     print("Tidak dapat diskon")
else:
     print("angka tidak valid")
