import sys
def kalkulator ():
    print("Pilih Operasi.")
    print("1.Jumlah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi")
    pilihan = input("Masukkan pilihan Anda(1/2/3/4): ")
    a1 = int(input("Masukkan bilangan pertama: "))
    a2 = int(input("Masukkan bilangan kedua: "))
    if pilihan == '1':
        tambah = a1 + a2
        print(a1,"+",a2,"=", tambah)
        kalkulator()
    elif pilihan == '2':
        kurang = a1 - a2
        print(a1,"-",a2,"=", kurang)
        kalkulator()
    elif pilihan == '3':
        kali = a1 * a2
        print(a1,"*",a2,"=", kali)
        kalkulator()
    elif pilihan == '4':
        bagi = a1 / a2
        print(a1,"/",a2,"=", bagi)
        kalkulator()

    elif pilihan == "q" or "Q" :
        sys.exit()
kalkulator()