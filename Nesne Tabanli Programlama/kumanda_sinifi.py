import random
import time

class Kumanda():

    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Acik":
            print("Televizyon zaten acik.")

        else:
            print("Televizyon aciliyor.")
            self.tv_durum="Acik"

    def tv_kapat(self):
        if self.tv_durum == "Kapali":
            print("Televizyon zaten kapali.")

        else:
            print("Televizyon kapaniyor.")
            self.tv_durum="Kapali"

    def ses_ayarlari(self):
        while True:
            girdi=input("Sesi acmak icin +, kismak icin ise -, cikis yapmak icin * basin : ")

            if girdi == "-":
                if self.tv_ses != 0:
                    self.tv_ses-=1
                    print("Ses : {}".format(self.tv_ses))

            elif girdi == "+":
                if self.tv_ses != 31:
                    self.tv_ses+=1
                    print("Ses : {}".format(self.tv_ses))

            else:
                print("Ses guncellendi.",self.tv_ses)
                break

    def kanal_ekle(self,kanal_adi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_adi)
        print("Kanal eklendi.")

    def rastgele_kanal(self):
        rand=random.randint(0,len(self.kanal_listesi)-1)

        self.kanal=self.kanal_listesi[rand]

        print("Suan ki kanal : ",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durumu : {}\n Tv ses : {}\n Kanal Listesi : {}\n Suan ki kanal : {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda=Kumanda()

print("""

**************************************

    Televizyon Uygulamasi
    
        1)Tv Ac
        2)Tv Kapat
        3)Ses Ayarlari
        4)Kanal Ekle
        5)Kanal Sayisini Ogrenme
        6)Rastgele Kanala Gecme
        7)Televizyon Bilgileri
        
        Cikmak icin 'q' ya basin...
        
**************************************

""")

while True:
    islem=input("Islemi secin : ")

    if islem == "q":
        break


    elif islem == "1":
        kumanda.tv_ac()

    elif islem == "2":
        kumanda.tv_kapat()

    elif islem == "3":
        kumanda.ses_ayarlari()

    elif islem == "4":
        kanal_isimleri=input("Kanal isimlarini ',' ile ayirarak giriniz : ")
        kanal_listesi=kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif islem == "5":
        print("Kanal sayisi : ",len(kumanda))

    elif islem == "6":
        kumanda.rastgele_kanal()

    elif islem == "7":
        print("Televizyon Bilgileri : \n",kumanda)

    else:
        print("Gecersiz islem.")
