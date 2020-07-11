print("""
***********************************************

\t\t Faktoriyel Bulma Programi

Cikmak icin 'q' ya basiniz.

***********************************************
""")

while True:
    sayi=input("Sayi giriniz : ")

    if sayi=="q":
        print("Program sonlandiriliyor...")
        break

    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(1, sayi + 1):
            faktoriyel *= i

        print("{} sayisinin faktoriyeli : {} \n".format(sayi, faktoriyel))
