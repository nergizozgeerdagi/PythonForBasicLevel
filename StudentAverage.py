cevap="e" or "E"
say=1
while cevap=="e" or "E":
  isim=input(str(say)+".Öğrencinin adını giriniz: ")
  not1=int(input("1. notunu giriniz: "))
  not2=int(input("2. notunu giriniz: "))

  ortalama=(not1+not2)/2
  print("Not Ortalamanız:",ortalama)
 
  say=say+1
  cevap=input("Başka bir öğrenci için ortalama hesaplamak ister misiniz? [e/E]vet/ [h/H]ayır: ")