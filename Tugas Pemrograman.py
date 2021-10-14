#Kelompok2
#Jeni Klistiana 17210608
#M. Alfi Nurpiansyah 17210836
#Dito Candra 17210346
#Dimas Imam 17210554


#Input Data
NIM = input(" Masukan NIM anda : ")
NamaMahasiswa = input(" Masukan Nama Mahasiswa : ")
Kelas = input(" Masukan Kode Kelas : ")
Mata_Kuliah = input(" Masukan Mata Kuliah : ")
Nilai_Absensi = float(input("Masukan Nilai Absensi : ")) #20%
Nilai_Tugas1 =  float(input("Masukan Nilai Tugas1 : ")) #10%
Nilai_Tugas2 = float(input("Masukan Nilai Tugas2 : ")) #10%
Nilai_UTS = float(input("Masukan Nilai UTS : ")) #30%
Nilai_UAS = float(input("Masukan Nilai UAS : ")) #30%
#Proses
NilaiAkhir = (0.2*Nilai_Absensi)+(0.1*Nilai_Tugas1)+(0.1*Nilai_Tugas2)+(0.3*Nilai_UTS)+(0.3*Nilai_UAS)
if NilaiAkhir >=80 :
    HurufNilai = "Grade A"
    print ("Grade A")
    print ("Selamat ANDA LULUS")
elif NilaiAkhir >=75 :
    HurufNilai = ("Grade B")
    print ("Grade B")
    print ("Selamat ANDA LULUS")
elif NilaiAkhir <=70 :
    HurufNilai = ("Grade C")
    print ("Grade C")
    print ("Maaf Anda Tidak Lulus")
elif NilaiAkhir <=60 :
    HurufNilai = ("Grade D")
    print ("Grade D")
    print ("Maaf Anda Tidak Lulus")
else :
    HurufNilai = ("Grade E")
    print ("Grade E")
    print ("Maaf Anda TIdak Lulus")
#Output
print ("===============================================")
print ("NIM : ", NIM)
print ("Nama Mahasiswa : ",NamaMahasiswa)
print ("Kelas :", Kelas)
print (" Mata Kuliah : ", Mata_Kuliah)
print ("Nilai Akhir : ",NilaiAkhir)
print ("Huruf Nilai : ", HurufNilai)












