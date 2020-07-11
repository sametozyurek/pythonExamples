def not_hesaplama(satir):
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = not1 * 0.3 + not2 * 0.3 + not3 * 0.4

    if son_not>=90:
        harf = "AA"

    elif son_not>=85:
        harf = "BA"

    elif son_not>=80:
        harf = "BB"

    elif son_not>=75:
        harf = "CB"

    elif son_not>=70:
        harf = "CC"

    elif son_not>=65:
        harf = "DC"

    elif son_not>=60:
        harf = "DD"

    elif son_not>=55:
        harf = "FD"

    else:
        harf = "FF"

    return isim + "------------>" + harf + "\n"

with open("dosya.txt","r") as file:

    eklenecekler_listesi=list()
    for i in file:
        eklenecekler_listesi.append(not_hesaplama(i))

    print(eklenecekler_listesi)

    with open("notlar.txt","w") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)