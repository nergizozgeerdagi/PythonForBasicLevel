# Python'da karar yapıları

isim=input("Öğrencinin adını giriniz:")
not1=int(input("1. notunu giriniz:"))
not2=int(input("2. notunu giriniz:"))

if not1<0 or not1>100 or not2<0 or not2>100:
  print("geçersiz not girdiniz")
else:
  ortalama=(not1*40/100)+(not2*60/100)
  print("Ders Ortalamanız:",ortalama)
  print("Akts Notunuz:")
  if ortalama>=85:
    print("A")
  elif ortalama>=80:
    print("B")
  elif ortalama>=70:
    print("C")
  elif ortalama>=65:
    print("D")
  elif ortalama>=60:
    print("E")
  else:
    print("F")

# klavyeden girilen 2 notun ortalamasının harf karşılığını ekrana yazan uygulamayı kodlayınız.