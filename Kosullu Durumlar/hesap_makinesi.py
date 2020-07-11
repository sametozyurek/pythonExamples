print("""
**********************

Islemler : 

1)Toplama islemi

2)Cikarma Islemi

3)Carpma Islemi

4)Bolme Islemi

**********************
""")

a=int(input("Ilk sayiyi girin : "))
b=int(input("Ikinci sayiyi girin : "))

c=int(input("Yapmak istediginiz islem numarasini giriniz : "))

if c==1 :
    print("Islem sonucu : {}".format(a + b))

elif c==2:
    print("Islem sonucu : {}".format(a - b))

elif c==3:
    print("Islem sonucu : {}".format(a*b))

elif c==4:
    print("Islem sonucu : {}".format(a / b))

else :
    print("Gecersiz islem numarasi girdiniz.")