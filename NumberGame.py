import random

bilgisayarinTuttuguSayi=random.randint(1,100)
#print(bilgisayarinTuttuguSayi)
denemeSayisi=0
while True:
  benimTahminEttigimSayi=int(input("Tuttuğum sayıyı tahmin et:"))
  denemeSayisi=denemeSayisi+1
  if bilgisayarinTuttuguSayi==benimTahminEttigimSayi:
    print("Tebrik ederim, {} denemede bildin.".format(denemeSayisi))
    break # döngüden çıkar
  elif bilgisayarinTuttuguSayi>benimTahminEttigimSayi:
    print("Daha büyük dene")
  else:
    print("Daha küçük dene")