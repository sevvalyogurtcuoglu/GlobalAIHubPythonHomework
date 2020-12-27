isim=input("isminizii giriniz : ")
soyisim=input("soyismizi giriniz : ")
d_yili=int(input("dogum ylinizi  giriniz : "))
meyve=[input("sevdiginiz meyveleri yazınız :")]
numara=int(input("numaranizi yaziniz : "))

bilgiler=[isim,soyisim,d_yili,meyve,numara]

for i in bilgiler:
    print(type(i))

