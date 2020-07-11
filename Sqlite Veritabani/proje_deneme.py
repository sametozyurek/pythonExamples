from kutuphane import *

print("""

*********************************************

    KUTUPHANE PROGRAMINA HOSGELDINIZ.
    
    ISLEMLER : 
        
        1) Kitaplari Goster
        2) Kitap Sorgulama
        3) Kitap Ekle
        4) Kitap Sil
        5) Baski Yukselt
        
    CIKMAK ICIN 'q' YA BASIN 

*********************************************

""")

kutuphane = Kutuphane()

while True:

    islem = input("\nIslem numarasini giriniz : \n")

    if islem == "q":
        print("Program sonlandiriliyor...")
        break

    elif islem == "1":
        kutuphane.kitaplari_goster()

    elif islem == "2":
        isim = input("Hangi kitabi istiyorsunuz : ")
        print("Kitap sorgulaniyor...\n")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)

    elif islem == "3":
        isim = input("Kitap ismi : ")
        yazar = input("Yazar ismi : ")
        yayinevi = input("Yayinevi : ")
        tur = input("Tur : ")
        baski = int(input("Baski : "))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)

        print("Kitap ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")

    elif islem == "4":
        isim = input("Hangi kitabi silmek istiyorsunuz : ")
        cevap = input("Emin misiniz? (E/H)")

        if cevap == "E":
            print("Kitap siliniyor...\n")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi.")

    elif islem == "5":
        isim = input("Hangi kitabin baskisini yukseltmek istiyorsunuz? : ")
        print("Baski yukseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)

    else:
        print("Gecersiz islem.")