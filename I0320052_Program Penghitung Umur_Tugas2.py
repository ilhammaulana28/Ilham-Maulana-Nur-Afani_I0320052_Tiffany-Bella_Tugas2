print("                   ===========================================")
print("                        Rancangan Program Penghitung Usia")
print("                   ===========================================\n\n")

tanggal_lahir = int(input("Masukkan tanggal lahir (Contoh : 28)     : "))
bulan_lahir = int(input("Masukkan bulan lahir (Contoh : 12)       : "))
tahun_lahir = int(input("Masukkan tahun lahir (Contoh : 2001)     : "))
print("\n")
print("                    ~~ Anda lahir pada", tanggal_lahir, "-", bulan_lahir, "-", tahun_lahir, "~~")
print("\n")
tanggal_sekarang = int(input("Masukkan tanggal sekarang (Contoh : 12)  : "))
bulan_sekarang = int(input("Masukkan bulan sekarang (Contoh : 2)     : "))
tahun_sekarang = int(input("Masukkan tahun sekarang (Contoh : 2021)  : "))
print("\n")
print("                    ~~ Sekarang tanggal", tanggal_sekarang, "-", bulan_sekarang, "-", tahun_sekarang, "~~")
print("\n")
date = 0
month = 0
year = abs(tahun_sekarang-tahun_lahir)

if (tanggal_lahir == tanggal_sekarang) and (bulan_lahir == bulan_sekarang):
    print("                  ~~ Selamat Ulang Tahun Yang ke,", year, "~~")
elif (tanggal_lahir == tanggal_sekarang) and (bulan_lahir < bulan_sekarang):
    year = tahun_sekarang - tahun_lahir
    month = bulan_sekarang - bulan_lahir
    date = 0
    print("Umur anda adalah", year, "tahun", month, "bulan", date, "hari")
elif (tanggal_lahir == tanggal_sekarang) and (bulan_lahir > bulan_sekarang):
    year = (tahun_sekarang - tahun_lahir) - 1
    month = 12 - (bulan_lahir - bulan_sekarang)
    date = 0
    print("Umur anda adalah", year, "tahun", month, "bulan", date, "hari")
elif (bulan_lahir == bulan_sekarang) and (tanggal_lahir < tanggal_sekarang):
    year = tahun_sekarang - tahun_lahir
    month = 0
    date = tanggal_sekarang - tanggal_lahir
    print("Umur anda adalah", year, "tahun", month, "bulan", date, "hari")
elif (bulan_lahir == bulan_sekarang) and (tanggal_lahir > tanggal_sekarang):
    year = (tahun_sekarang - tahun_lahir) - 1
    month = 11
    if (bulan_sekarang == 1, 3, 5, 7, 8, 10, 12):
        date = 31 - (tanggal_lahir - tanggal_sekarang)
        if bulan_sekarang == 2:
            date = 28 - (tanggal_lahir - tanggal_sekarang)
        else:
            date = 30 - (tanggal_lahir - tanggal_sekarang)

elif (tanggal_lahir < tanggal_sekarang) and (bulan_lahir < bulan_sekarang):
    year = tahun_sekarang - tahun_lahir
    month = bulan_sekarang - bulan_lahir
    if (bulan_sekarang == 1, 3, 5, 7, 8, 10, 12):
        date = 31 - (tanggal_sekarang - tanggal_lahir)
        if bulan_sekarang == 2:
            date = 28 - (tanggal_sekarang - tanggal_lahir)
        else:
            date = 30 - (tanggal_sekarang - tanggal_lahir)

elif (tanggal_lahir < tanggal_sekarang) and (bulan_lahir > bulan_sekarang):
    year = (tahun_sekarang - tahun_lahir) - 1
    month = 12 - (bulan_lahir - bulan_sekarang)
    if (bulan_sekarang == 1, 3, 5, 7, 8, 10, 12):
        date = (31 - tanggal_sekarang) + tanggal_lahir
        if bulan_sekarang == 2:
            date = (28 - tanggal_sekarang) + tanggal_lahir
        else:
            date = (30 - tanggal_sekarang) + tanggal_lahir

elif (tanggal_lahir > tanggal_sekarang) and (bulan_lahir < bulan_sekarang):
    year = tahun_sekarang - tahun_lahir
    month = (bulan_sekarang - bulan_lahir) - 1
    if (bulan_lahir == 1, 3, 5, 7, 8, 10, 12):
        date = (31 - tanggal_lahir) + tanggal_sekarang - 1
        if bulan_lahir == 2:
            date = (28 - tanggal_sekarang) + tanggal_lahir - 1
        else:
            date = (30 - tanggal_sekarang) + tanggal_lahir - 1

elif (tanggal_lahir > tanggal_sekarang) and (bulan_lahir > bulan_sekarang):
    year = (tahun_sekarang - tahun_lahir) - 1
    month = 12 - (bulan_lahir - bulan_sekarang) - 1
    if (bulan_sekarang == 1, 3, 5, 7, 8, 10, 12):
        date = 31 - (tanggal_lahir - tanggal_sekarang)
        if bulan_sekarang == 2:
            date = 28 - (tanggal_lahir - tanggal_sekarang)
        else:
            date = 30 - (tanggal_lahir - tanggal_sekarang)
print("\n")
print("~~Umur anda adalah", year, "tahun", month, "bulan", date, "hari~~")
print("\n\n")
input("Press any key to continue...")