print("""

*****************************************************

        Sayinin tam bolenlerini bulan program
        
*****************************************************

""")

def bolenler(sayi):
    liste = list()
    for i in range(1,sayi+1):
        if sayi % i ==0:
            liste.append(i)
    print("{} sayisini tam bolenleri : {}".format(sayi,liste))


while True:

    girdi=input("Sayiyi girin : ")

    if girdi=="q":
        break

    else:
        bolenler(int(girdi))