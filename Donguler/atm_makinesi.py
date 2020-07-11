print("""
*********************************************

ATM Makinesine Hosgeldiniz.

\tIslemler ;

\t\t1. Bakiye Sorgulama

\t\t2. Para Yatirma

\t\t3. Para Cekme

Programdan cikmak icin 'q' ya basin.

*********************************************
""")

bakiye=0

while True:

    islem=input("Yapmak istediginiz islemi seciniz : ")

    if islem=="q":

        print("Bizi tercih ettiginiz icin tesekkurler.\n")
        break

    elif islem=="1":

        print("Bakiyeniz {} tl'dir\n".format(bakiye))

    elif islem=="2":

        miktar=int(input("Girmek istediginiz miktari giriniz : "))

        bakiye+=miktar
        print("Para yatirma isleminiz basarili.\n")

    elif islem=="3":

        miktar=int(input("Cekmek istediginiz miktari giriniz : "))

        if bakiye-miktar<0:
            print("Yeterli bakiye bulunmuyor.\n")
            continue

        bakiye -= miktar
        print("Para cekme islemi basarili.\n")

    else:
        print("Girdiginiz islem gecersiz...\n")