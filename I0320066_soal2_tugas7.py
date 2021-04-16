print("="*40)
print("Program Menghitung Tinggi Badan Siswa")
print("="*40)

tinggi_siswa = input("Masukkan tinggi badan siswa (pisahkan dengan spasi): ").split()

for i in range(len(tinggi_siswa)):
    tinggi_siswa[i] = int(tinggi_siswa[i])

print("Tinggi badan yang diinput : ", tinggi_siswa)
print("="*40)

rata_rata = sum(tinggi_siswa)/len(tinggi_siswa)
print("Rata-rata tinggi badan siswa adalah ", rata_rata)

import math
print("Tinggi badan yang paling tinggi adalah ", max(tinggi_siswa))

print("Tinggi badan yang paling rendah adalah ", min(tinggi_siswa))

print("Rata-rata tinggi badan dengan pembulatan ke atas adalah ", math.ceil(rata_rata))

print("Rata-rata tinggi badan dengan pembulatan ke bawah adalah ", math.floor(rata_rata))