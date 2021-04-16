print("="*25)
print("Program Kalimat Sapaan")
print("="*25)

sapaan = input("Masukkan kalimat sapaan anda: ")
print("Kalimat sapaan anda: ", sapaan)
print("Jumlah huruf kalimat sapaan anda: ", len(sapaan), "huruf")

kapital = sapaan.capitalize()
print("Kalimat sapaan anda berawalan kapital: ", kapital)

center = sapaan.center(40,"*")
print("Kalimat sapaan anda dalam center: ", center)

sapaan1 = sapaan.upper()
sapaan2 = sapaan.lower()
print("Kalimat sapaan anda dalam huruf kapital: ", sapaan1)
print("Kalimat sapaan anda dalam huruf kecil: ", sapaan2)

a = sapaan.count("a")
i = sapaan.count("i")
u = sapaan.count("u")
e = sapaan.count("e")
o = sapaan.count("o")
print("Jumlah huruf a dalam kalimat sapaan anda = ", a, "huruf")
print("Jumlah huruf i dalam kalimat sapaan anda = ", i, "huruf")
print("Jumlah huruf u dalam kalimat sapaan anda = ", u, "huruf")
print("Jumlah huruf e dalam kalimat sapaan anda = ", e, "huruf")
print("Jumlah huruf o dalam kalimat sapaan anda = ", o, "huruf")

