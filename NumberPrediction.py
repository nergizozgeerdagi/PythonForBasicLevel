import random

enKucukDeger=1
enBuyukDeger=100
while True:
  print("{}-{}".format(enKucukDeger,enBuyukDeger))
  bilgisayarinTahminEttigiSayi=random.randint(enKucukDeger,enBuyukDeger)

  cevap=input("{} senin tuttuğun sayı mı? [e]vet / daha [b]üyük / daha [k]üçük: ".format(bilgisayarinTahminEttigiSayi))

  if cevap=="e":
    print("Bildim!")
    break
  elif cevap=="b":
    enKucukDeger=bilgisayarinTahminEttigiSayi+1
  else:
    enBuyukDeger=bilgisayarinTahminEttigiSayi-1