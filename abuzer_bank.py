print("""
------>  AbuzerBank <------ 

------> Verison 3 <------ 
------>  Mehmet Kahya <------ 

----> Son Düzenlenme Tarihi: 23.07.2021 <----

------>  Yazılma Tarihleri = 8.06.2021 - 9.06.2021 - 10.06.2021 - 11.06.2021 ----------------------------- 22.07.2021 - 23.07.2021  <------ 


--> En son eklenen özellikler;

        1- yeni kullanıcı oluşturma
        2- her kullanıcı için farklı bakiye
        3- eğer kullanıcı belirlenen listede yoksa ve giriş yapmaya(1) çalışırsa sistem kapanır ve tekrar deneyin yazar"
        4. Admin hesaplar(ana listedeki kişiler) için sabit para kaydetme.
        5. Kredi çekme sistemi oluşturma
        6. krediyi geri ödeme
        7. geri ödenirken faiz alınması 
        8. para transferi
        9. Yeni admin ekleme paneli
        10. Farklı Para Birimleri İle İşlem Yapma (Kredi ödeme, para çekme, parayı bozdurma vs )    


--> Tarihlere göre toplam kod satırları;

        1.gün ort. 30 satır.
        2.gün 121 satır.
        3.gün 423 satır.
        4.gün  600 satır.
        22.07.2021    638 satır
        23.07.2021    646 satır
  

--> Eklenemeyi düşündüğüm özellikler;
 
            ------- {} -------  

-- AbuzerBank Tüm Telif Hakları Saklıdır 2021 -- 

<------------------------------------------------------------------------------------------------------------------------------------------------------------->
""")

import random
import time
import math

soru2 = int(input("Kredi Çekmek için 1 \nİşlem yapmak için 2\nKredi Ödemek için 3\nPara Transferi için 4' e basınız: "))

if soru2 == 1:


    kisi = ["mehmet","Mehmet","MEHMET","ege","abuzer","onat","q"]
    hesapno = [123,321,342]

    isim = str(input("İsminizi Girin: "))
    numara = int(input("Hesap numaranızı girin: "))


    if isim in kisi:
        print("İsim Doğru ")

    else:
        print("Tekrar Dene, Giriş Yapılamadı")
        exit()

    if numara in hesapno:
        print("Numara Doğru")
        print("Hesaba giriliyor...........")
        time.sleep(1.1)
        print("Hesabınız:")
    else:
        print("!!!! Tekrar Dene, Giriş Yapılamadı !!!!")
        exit()

    class Account:
        def __init__(self,isim,numara,bakiye):
            self.isim = isim
            self.numara = numara
            self.bakiye = bakiye

        def hesapBilgileri(self):
            print("İsim: ",self.isim)
            print("Numara: ",self.numara)
            print("Bakiye: ",self.bakiye)

        def paraCek(self,miktar):
            if(self.bakiye - miktar < 0):
                print("Bu miktarda kredi alamazsınız!")
            else:
                self.bakiye -= miktar
                print("Yeni Bakiye", self.bakiye)
        def paraYatir(self, miktar):
            self.bakiye += miktar
            print("Yeni Bakiye: ",self.bakiye)
            if self.bakiye == 0:
                print("!!!! HESABINIZDA PARA KALMADI !!!!")

            if self.bakiye < 0:
                print("Borca girdiniz!")
                            
            if self.bakiye > 1000:
                print("Krediniz Onaylandı!")

                                              
                                            
    total = random.randint(0,1000)
    account = Account(isim, numara, total)
    account.hesapBilgileri()  
    borc = account.paraYatir(int(input("Kredi miktarları: \n 100tl için 100 yazınız:  \n 1.000tl için 1000 yazınız: \n 10.000tl için 10000 yazınız: ")))
    if borc == 100:
        (total+100)
    if borc == 1000:
        (total+1000)
    if borc == 10000:
        (total+10000)



 
    class Account:
        def __init__(self,isim,numara,bakiye):
            self.isim = isim
            self.numara = numara
            self.bakiye = bakiye

        def hesapBilgileri(self):
            print("İsim: ",self.isim)
            print("Numara: ",self.numara)
            print("Bakiye: ",self.bakiye)

        def paraCek(self,miktar):
            if(self.bakiye - miktar < 0):
                print("Yetersiz Bakiye")
            else:
                self.bakiye -= miktar
                print("Yeni Bakiye", self.bakiye)
        def paraYatir(self, miktar):
            self.bakiye += miktar
            print("Yeni Bakiye: ",self.bakiye)
            if self.bakiye == 0:
                print("!!!! HESABINIZDA PARA KALMADI !!!!")

            if self.bakiye < 0:
                print("Borca girdiniz!")
                            
            if self.bakiye > 1000:
                print("tebrikler kâra geçtiniz!")

                                                

    account.hesapBilgileri()
    zaman = ["3 ay","5 ay","6 ay","8 ay", "1 yıl"]
    surehesap = random.choice(zaman)
    borc = print("Krediniz %20 Faizlidir ve son ödeme tarihi {} sonradır.".format(surehesap))
 
    exit()   



if soru2 == 2:

    soru = int(input("Giriş(1) \nKaydol(2): \nAdmin(3) girişi: \nPara Bozdurmak(4): "))
    kisi = ["mehmet","Mehmet","MEHMET","ege","abuzer","onat"]
    hesapno = [123,321,342]
    if soru == 1: 

        isim = str(input("İsminizi Girin: "))
        numara = int(input("Hesap numaranızı girin: "))



        if isim in kisi:
            print("İsim Doğru ")

        else:
            print("Tekrar Dene, Giriş Yapılamadı")
            exit()

        if numara in hesapno:
            print("Numara Doğru")
            print("Hesaba giriliyor...........")
            time.sleep(1.1)
            print("Hesabınız:")
        else:
            print("!!!! Tekrar Dene, Giriş Yapılamadı !!!!")
            exit()



        class Account:
            def __init__(self,isim,numara,bakiye):
                self.isim = isim
                self.numara = numara
                self.bakiye = bakiye

            def hesapBilgileri(self):
                print("İsim: ",self.isim)
                print("Numara: ",self.numara)
                print("Bakiye: ",self.bakiye)

            def paraCek(self,miktar):
                if(self.bakiye - miktar < 0):
                    print("Yetersiz Bakiye")
                else:
                    self.bakiye -= miktar
                    print("Yeni Bakiye", self.bakiye)
            def paraYatir(self, miktar):
                self.bakiye += miktar
                print("Yeni Bakiye: ",self.bakiye)
                if self.bakiye == 0:
                    print("!!!! HESABINIZDA PARA KALMADI !!!!")

                if self.bakiye < 0:
                    print("Borca girdiniz!")
                            
                if self.bakiye > 1000:
                    print("tebrikler kâra geçtiniz!")

                                                
        total = random.randint(0,1000)                                
        account = Account(isim, numara, total)
        account.hesapBilgileri()
        borc = account.paraYatir(int(input("İşlem için birim giriniz! : ")))
        exit()   



    if soru == 2: 
        kisi.append(input(str("Kayıt için isminizi Girin: ")))
        hesapno.append(int(input("Kayıt için kendi oluşturacağınız numarayı girin: ")))
        isim = str(input("İsminizi Girin: "))
        numara = int(input("Hesap numaranızı girin: "))



        if isim in kisi:
            print("İsim Doğru ")

        else:
            print("Tekrar Dene, Giriş Yapılamadı")
            exit()

        if numara in hesapno:
            print("Numara Doğru")
            print("Hesaba giriliyor...........")
            time.sleep(1.1)
            print("Hesabınız:")
        else:
            print("!!!! Tekrar Dene, Giriş Yapılamadı !!!!")
            exit()

        class Account:
            def __init__(self,isim,numara,bakiye):
                self.isim = isim
                self.numara = numara
                self.bakiye = bakiye

            def hesapBilgileri(self):
                print("İsim: ",self.isim)
                print("Numara: ",self.numara)
                print("Bakiye: ",self.bakiye)

            def paraCek(self,miktar):
                if(self.bakiye - miktar < 0):
                    print("Yetersiz Bakiye")
                else:
                    self.bakiye -= miktar
                    print("Yeni Bakiye", self.bakiye)
            def paraYatir(self, miktar):
                self.bakiye += miktar
                print("Yeni Bakiye: ",self.bakiye)
                if self.bakiye == 0:
                    print("!!!! HESABINIZDA PARA KALMADI !!!!")

                if self.bakiye < 0:
                    print("Borca girdiniz!")
                        
                if self.bakiye > 1000:
                    print("tebrikler kâra geçtiniz!")

    

        total = random.randint(0,1000)                                
        account = Account(isim, numara, total)
        account.hesapBilgileri()
        borc = account.paraYatir(int(input("İşlem için birim giriniz! : ")))   




    if soru == 3: 

        isim = str(input("Admin Kullanıcı Adı: "))
        numara = int(input("Admin Şifre: "))



        if isim in kisi:
            print("Adminlik Onaylandı ")

        else:
            print("Tekrar Dene, Giriş Yapılamadı")
            exit()

        if numara in hesapno:
            print("Şifre Doğru")
            print("Hesaba giriliyor...........")
            time.sleep(1.1)
            print("Admin Hesabınız: \n")
        else:
            print("!!!! Tekrar Dene, Giriş Yapılamadı !!!!")
            exit()

        if isim == "mehmet":
            print("Adminlik seviyesi 10/10 , Kodu yazan kişi ")
            yeni = int(input("Yeni Admin Ekleme Panali için 1'i, Normal işlem için 0'ı tuşlayın "))
            if yeni == 1:
                print("---------- Yeni Admin Ekleme Paneline Hoş Geldin Mehmet! ----------")
                kisi = ["mehmet","Mehmet","MEHMET","ege","abuzer","onat"]
                hesapno = [123,321,342]
                kisi.append(input(str("Yeni Adminin Kullanıcı Adı: ")))
                hesapno.append(int(input("Yeni Adminin Şifresi: ")))


                print("Kontrol için Yeni Admin Hesabına Giriliyor..")
                time.sleep(2)
                isim = input("Admin Kullanıcı Adı: ")
                numara = int(input("Admin Şifre: "))


                if isim in kisi:
                    print("İsim Doğru")

                else:
                    print("Başarısız!")

                if numara in hesapno:
                    print("Numara Doğru!")
                
                else:
                    print("Yanlış!")
            if yeni == 0:
                    
                class Account:
                    def __init__(self,isim,numara,bakiye):
                        self.isim = isim
                        self.numara = numara
                        self.bakiye = bakiye

                    def hesapBilgileri(self):
                        print("İsim: ",self.isim)
                        print("Numara: ",self.numara)
                        print("Bakiye: ",self.bakiye)

                    def paraCek(self,miktar):
                        if(self.bakiye - miktar < 0):
                            print("Yetersiz Bakiye")
                        else:
                            self.bakiye -= miktar
                            print("Yeni Bakiye", self.bakiye)
                    def paraYatir(self, miktar):
                        self.bakiye += miktar
                        print("Yeni Bakiye: ",self.bakiye)
                        if self.bakiye == 0:
                            print("!!!! HESABINIZDA PARA KALMADI !!!!")

                        if self.bakiye < 0:
                            print("Borca girdiniz!")
                                    
                        if self.bakiye > 1000:
                            print("tebrikler kâra geçtiniz!")

                


                account = Account(isim, numara, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
                account.hesapBilgileri()
                borc = account.paraYatir(int(input("İşlem için birim giriniz! : ")))   



        if isim == "ege":
            print("Adminlik seviyesi 5/10")
            

            class Account:
                def __init__(self,isim,numara,bakiye):
                    self.isim = isim
                    self.numara = numara
                    self.bakiye = bakiye

                def hesapBilgileri(self):
                    print("İsim: ",self.isim)
                    print("Numara: ",self.numara)
                    print("Bakiye: ",self.bakiye)

                def paraCek(self,miktar):
                    if(self.bakiye - miktar < 0):
                        print("Yetersiz Bakiye")
                    else:
                        self.bakiye -= miktar
                        print("Yeni Bakiye", self.bakiye)
                def paraYatir(self, miktar):
                    self.bakiye += miktar
                    print("Yeni Bakiye: ",self.bakiye)
                    if self.bakiye == 0:
                        print("!!!! HESABINIZDA PARA KALMADI !!!!")

                    if self.bakiye < 0:
                        print("Borca girdiniz!")
                                
                    if self.bakiye > 1000:
                        print("tebrikler kâra geçtiniz!")

            


            account = Account(isim, numara, 100000000)
            account.hesapBilgileri()
            borc = account.paraYatir(int(input("İşlem için birim giriniz! : ")))   



        if isim == "onat":
            print("Adminlik seviyesi 1/10  \n")
            class Account:
                def __init__(self,isim,numara,bakiye):
                    self.isim = isim
                    self.numara = numara
                    self.bakiye = bakiye

                def hesapBilgileri(self):
                    print("İsim: ",self.isim)
                    print("Numara: ",self.numara)
                    print("Bakiye: ",self.bakiye)

                def paraCek(self,miktar):
                    if(self.bakiye - miktar < 0):
                        print("Yetersiz Bakiye")
                    else:
                        self.bakiye -= miktar
                        print("Yeni Bakiye", self.bakiye)
                def paraYatir(self, miktar):
                    self.bakiye += miktar
                    print("Yeni Bakiye: ",self.bakiye)
                    if self.bakiye == 0:
                        print("!!!! HESABINIZDA PARA KALMADI !!!!")

                    if self.bakiye < 0:
                        print("Tebrikler hâla Borçtasınız!!!!!")
                                
                    if self.bakiye > 1000:
                        print("tebrikler kâra geçtiniz!")

            

            account = Account(isim, numara, -10000000000)
            account.hesapBilgileri()
            borc = account.paraYatir(int(input("Borçtan kurtulmak için bankaya para ödeyin, ödenecek para: "))) 
# Para bozdurma kısmı
    if soru == 4:
        borsa = int(input("Bozdurmak İstediğiniz para birimini seçin: \n USD (1) \n EUR(2):  "))
        para1 = int(input("Ne kadar para bozdurmak istiyorsunuz: "))

        usd = (8)
        eur = (11)
        sonucusd = (int(para1*usd))
        if borsa == 1:
            print("{} TL Hesabınıza Aktarılıyor..".format(sonucusd))
            time.sleep(2)
            print("Hesabınıza Aktarım Başarılı!")

        if borsa == 2:
            print("{} TL Hesabınıza Aktarılıyor..".format(sonucusd))
            time.sleep(2)
            print("Hesabınıza Aktarım Başarılı!")

if soru2 == 3:
    print("Ödeme kısmına hoşgeldiniz!")
    kisi = ["mehmet","Mehmet","MEHMET","ege","abuzer","onat","q"]
    hesapno = [123,321,342]
    krediNo = [100,200,1000,2000,300,3000]
    krediBirim = [100,1000,10000]

    isim = str(input("İsminizi Girin: "))
    numara = int(input("Hesap numaranızı girin: "))
    kredino = int(input("Kredi Numaranızı girin: "))

    if isim in kisi:
        print("İsim Doğru\n ")

    else:
        print("Tekrar Dene, Giriş Yapılamadı")
        exit()

    if kredino in krediNo:
        print("Kredi numaranız doğru!\n")
    else:
        print("Tekrar Dene, Giriş Yapılamadı")
        exit()

    if numara in hesapno:
        print("Numara Doğru\n")
        print("Hesaba giriliyor...........")
        time.sleep(1.1)
        print("Hesabınız:\n")
    else:
        print("!!!! Tekrar Dene, Giriş Yapılamadı !!!!")
        exit()

      
    class Account:
        def __init__(self,isim,numara,bakiye):
            self.isim = isim
            self.numara = numara
            self.bakiye = bakiye

        def hesapBilgileri(self):
            print("İsim: ",self.isim)
            print("Numara: ",self.numara)
            print("Ödenecek Kredi %200 Faiz ile birlikte: ",self.bakiye)

        def paraCek(self,miktar):
            if(self.bakiye - miktar < 0):
                print("Yetersiz Bakiye")
            else:
                self.bakiye -= miktar
                print("Kalan Kredi: ", self.bakiye)
        def paraYatir(self, miktar):
            self.bakiye += miktar
            print("Kalan Kredi: ",self.bakiye)

            if self.bakiye == 0:
                 print("\n!!!! KREDİYİ GERİ ÖDEME BAŞARILI, ABUZERBANK'A HERHANGİ BİR BORCUNUZ KALMAMIŞTIR !!!!\n")

            if self.bakiye < 0:
                print("Fazla ödeme yaptınız, fazla ödemeniz, bankamız tarafından size geri gönderilicektir -AbuzerBank-!")
                        
            if self.bakiye > 1000:
                print("Hatalı İşlem!")
                exit()

                
    total = random.choice(krediBirim)                                
    account = Account(isim, numara, total)
    account.hesapBilgileri()
    borc = account.paraYatir(int(input("Krediyi ödemek için tutar giriniz! : ")))   


if soru2 == 4:
    print("Para transferine hoşgeldiniz !")

    kisi = ["mehmet","Mehmet","MEHMET","ege","abuzer","onat","q"]
    hesapno = [123,321,342,100,1000,20]
    karsıhesapNo = [123,321,342,100,1000,20]

    gönderilecekKisi = ["mehmet","Mehmet","MEHMET","ege","abuzer","onat","q","abdurrezak"]


    isim = str(input("İsminizi Girin: "))
    numara = int(input("Hesap numaranızı girin: "))
    gönderim = str(input("Gönderilecek kişiyi yazınız: "))
    gönderimno = int(input("Göndereceğiniz kişinin hesap numarasını giriniz: "))
    gönderimBirim = [100,1000,10000]
    if isim in kisi:
        print("İsim Doğru ")

    else:
        print("Tekrar Dene, Giriş Yapılamadı")
        exit()

    if gönderim in  gönderilecekKisi:
        print("Kredi numaranız doğru!")
    else:
        print("Tekrar Dene, Giriş Yapılamadı")
        exit()

    if gönderimno in karsıhesapNo:
        print("Karşı tarafın hesap numarası doğru!")
    else:
        print("Tekrar dene hatalı işlem")
        exit()

    if numara == gönderimno:
        print("Sizin hesap numaranız ile karşı tarafınki aynı olamaz! TEKRAR deneyin!")
        exit()

    if numara in hesapno:
        print("Numara Doğru")
        print("Hesaba giriliyor...........")
        time.sleep(1.1)
        print("Hesabınız:")
    else:
        print("!!!! Tekrar Dene, Giriş Yapılamadı !!!!")
        exit()

    class Account:
        def __init__(self,isim,numara,bakiye,gönderim,gönderimno):
            self.isim = isim
            self.numara = numara
            self.bakiye = bakiye
            self.gönderim = gönderim
            self.gönderimno = gönderimno

        def hesapBilgileri(self):
            print("İsim: ",self.isim)
            print("Numara: ",self.numara)
            print("Bakiyen: ",self.bakiye)
            print("Gönderilecek Kişi: ",self.gönderim)
            print("Gönderilcek Kişinin Hesap Numarası: ",self.gönderimno)


        def paraCek(self,miktar):
            if(self.bakiye - miktar < 0):
                print("Yetersiz Bakiye")
            else:
                self.bakiye -= miktar
                print("Para Gönderimi Başarılı Kalan paran: ", self.bakiye)
        def paraYatir(self, miktar):
            self.bakiye += miktar
            print("Para Gönderimi Başarılı Kalan paran: ",self.bakiye)

            if self.bakiye == 0:
                 print("\n!!!! Gönderim Başarılı!!!!\n")

            if self.bakiye < 0:
                print("Bakiyenizden fazla para gönderdiniz lütfen tekrar deneyin")
                        
            if self.bakiye > total:
                print("Hatalı İşlem!")
                exit()


                
    total = random.randint(0,10000)                              
    account = Account(isim, numara, total, gönderim, gönderimno)
    account.hesapBilgileri()
    borc = account.paraYatir(int(input("Karşı tarafa gönderilecek parayı yazınız\n 100tl\n 1.000tl\n 10.000tl : ")))
