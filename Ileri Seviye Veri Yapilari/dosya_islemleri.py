class Dosya():
    def __init__(self):
        with open("metin.txt","r") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()

            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("/n")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip(" ")
                i = i.strip("!")
                i = i.strip(";")

                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        self.kelimeler_kumesi = set()

        for i in self.sade_kelimeler:
            self.kelimeler_kumesi.add(i)

        ##print("\nTum Kelimeler ================>\n")
        ##for i in self.kelimeler_kumesi:
          ##  print(i)
            ##print("********************************************")

    def kelime_ara(self,aranan):

        try:
            if self.sade_kelimeler.index(aranan):
                print("\n{} kelimesi metinde var.".format(aranan))
            else:
                pass
        except ValueError:
            print("\n{} kelimesi metinde yok.".format(aranan))

    def kelime_frekansi(self):
        kelime_sozluk = dict()

        for i in self.sade_kelimeler:
            if i in kelime_sozluk:
                kelime_sozluk[i] += 1

            else:
                kelime_sozluk[i] = 1
        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geciyor.".format(kelime,sayi))
            print("**********************************************")

dosya = Dosya()
dosya.tum_kelimeler()
dosya.kelime_ara("she")