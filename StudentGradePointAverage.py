ogrenciSayisi=int(input("Kaç öğrenci için ortalama hesaplamak istersiniz?"))

while ogrenciSayisi>0:
  isim=input("Öğrencinin adını giriniz:")
  not1=int(input("1. notunu giriniz:"))
  not2=int(input("2. notunu giriniz:"))

  ortalama=(not1+not2)/2
  print("Girdiğiniz Öğrencinin Ortalaması:",ortalama)
  print("\n")
  ogrenciSayisi=ogrenciSayisi-1