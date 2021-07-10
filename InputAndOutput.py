isim=input("Lütfen isminizi giriniz: ")
print("Merhaba",isim)
kullaniciAdi=input("Kullanici adinizi giriniz: ")
sifre=input("Sifrenizi giriniz: ")
if kullaniciAdi=="nergiz.erdagi" and sifre=="1236":
  print("Giriş başarılı!")
else:
  print("Kullanıcı adı ya da şifre hatalı, yeniden deneyiniz!")
#and
#1 and 1=1
#1 and 0=0
#0 and 1=0
#0 and 0=0
###############
#or
#1 or 1=1
#1 or 0=1
#0 or 1=1
#0 or 0=0