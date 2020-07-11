import random
import time

print("""

*************************

    Sayi Tahmin Oyunu
    
    1 ile 40 arasinda sayi tahmin edin.
    
*************************

""")

rand_sayi=random.randint(1,40)
tahmin_hakki=5
while True:
    sayi=int(input("Sayi Girin : "))

    if sayi < rand_sayi:
        print("Sonuclar geliyor...")
        time.sleep(1)

        print("Daha yuksek bir sayi girin...\n")
        tahmin_hakki-=1

    elif sayi > rand_sayi:
        print("Sonuclar geliyor...")
        time.sleep(1)

        print("Daha kucuk bir sayi girin...\n")
        tahmin_hakki-=1

    else:
        print("Sonuclar geliyor...")
        time.sleep(1)

        print("Tebrikler! Oyunu kazandiniz... \n Sayi : {}".format(rand_sayi))
        break

    if tahmin_hakki <=0:
        print("Tahmin hakkiniz doldu. Oyunu kazanamadiniz...")

        print("Sayi : {}".format(rand_sayi))
        break