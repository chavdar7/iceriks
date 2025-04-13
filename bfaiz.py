print("Bileşik faiz hesabına hoşgeldiniz!!!\n")

anapara = int(input("ana paranızı giriniz: "))
faiz_oran = float(input("yıllık faiz oranını giriniz: "))
yıl = int(input("kaç yıllık tutacağınızı giriniz: "))

i=1

while i <= yıl:
    anapara += (anapara * faiz_oran)/100
    i += 1

print(f"{yıl} yıl sonunda son paranız : {anapara}")