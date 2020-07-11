print("""

*******************************

    Asal Sayilar Programi

*********************************

""")

def asal_sayi(sayi):
    if sayi==1:
        return False

    elif sayi==2:
        return True

    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                return False
        return True

while True:
    girdi=input("Sayi girin : ")

    if girdi=="q":
        break

    else:
        girdi=int(girdi)

        if asal_sayi(girdi):
            print("Sayi asaldir.")

        else:
            print("Sayi asal degildir.")