print ("----------------------------")
print ("Nama : Vebronia vitania lusi")
print ("NIM : 2409116112")
print ("----------------------------")

# masukan nama dan password

while True:
    print("Halo, selamat datang vebromart")
    nama = input("masukan nama:")
    password = input("masukan password:")
    if nama == "asva" and password == "020806":
        print("anda terverifikasi masuk")
        break
    else:
        print("anda gagal terverifikasi silahkan masukan nama dan password anda dengan benar")

# Inputan
while True:
    harga = int(input('masukan harga barang :'))
    jumlah = int(input('masukan Jumlah barang :'))

    Total_harga = harga * jumlah

    if harga > 250000:
        diskon = harga * 25/100
        total = harga - diskon 
        print('=== anda mendapatkan diskon sebesar 25% ===')
    elif harga < 250000:
        total = harga 
        print('=== anda tidak mendapatkan diskon')

    print('total harga yang harus di bayar :')

# Apakah ingin berbelanja lagi

    Lanjut = input("ingin berbelanja lagi? (ya/tidak) :")  
    if Lanjut.lower() != "y" :
        print("ghamsamida!!!!")
        break