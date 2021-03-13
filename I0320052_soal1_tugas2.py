print("                        =================================\n")
print("                        PROGRAM SEDERHANA MENGHITUNG LUAS\n")
print("                        =================================\n")
input("")
print("1. Menghitung luas persegi panjang")
p = int(input("Masukkan nilai panjang          : "))
L = int(input("Masukkan nilai lebar            : "))
luas_pp = p * L
print("Luas persegi panjang adalah", luas_pp, "\n")
print("=============================================\n")
print("2. Menghitung luas lingkaran")
phi = 22/7
r = int(input("Masukkan panjang jari-jari       : "))
luas_ling = phi * r * r
print("Luas lingkaran adalah", luas_ling, "\n")

print("=============================================\n")

print("3. Menghitung luas permukaan kubus")
s = int(input("Masukkan panjang rusuk kubus     : "))
luas_kubus = s * s * 8
print("Luas permukaan kubus adalah", luas_kubus, "\n")

print("=============================================\n")

print("4. Konversi suhu celcius ke fahrenheit")
c = int(input("Masukkan suhu celcius            : "))
konversi1 = (9*c/5) + 32
print("Suhu dalam fahrenheit adalah", konversi1, "\n")

print("=============================================\n")

print("5. Konversi suhu reamur ke kelvin")
reamur = int(input("Masukkan suhu reamur        : "))
konversi2 = (5*reamur/4) + 273
print("Suhu dalam kelvin adalah", konversi2, "\n\n")
input("Press any key to continue...")