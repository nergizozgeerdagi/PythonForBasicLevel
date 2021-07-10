ogrenciAd=input("Öğrenci adını giriniz: ")
not1=int(input("1. notu giriniz: "))
not2=int(input("2. notu giriniz: "))
ortalama=((not1*40/100)+(not2*60/100))
print("Öğrencinin ortalaması: ",ortalama)
if ortalama>=60:
  print("Öğrenci dersten geçti")
else:
  print("Öğrenci dersten kaldı")