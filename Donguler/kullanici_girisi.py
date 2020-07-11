print("""
***********************************************

\t\t Kullanici Girisi Programi

***********************************************
""")

sys_kullanici_adi="samet"
sys_parola="12345"

giris_hakki=3

while True:
    k_adi=input("\nKullanici Adi :  ")
    parola=input("Paralo : ")

    if sys_kullanici_adi!=k_adi and sys_parola==parola:
        print("Kullanici Adi hatali!")
        giris_hakki-=1

    elif sys_kullanici_adi==k_adi and sys_parola!=parola:
        print("Parola hatali!")
        giris_hakki-=1

    elif sys_kullanici_adi!=k_adi and sys_parola!=parola:
        print("Kullanici Adi ve Parola hatali!")
        giris_hakki-=1

    else:
        print("Sisteme basarili bir sekilde giris yapildi.")
        break

    if giris_hakki==0:
        print("Giris hakkiniz bitti. Daha sonra tekrar deneyin.")
        break
