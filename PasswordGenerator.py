import random
kucukHarf = "abcdefghijklmnopqrstuvwxyz"
buyukHarf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar = "0123456789"
semboller = "{}[]()*/\,.-_=:;"
olustur = buyukHarf + kucukHarf + sayilar + semboller
sifreUzunluk = 16
sifre = "".join(random.sample
(olustur,sifreUzunluk))
print(sifre)