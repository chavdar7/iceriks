print("HESAP MAKİNESİNE HOŞGELDİNİZ")
print("*"*35)

print("Önce 1. sayıyı sonra yapmak istediğiniz işlemin numarasını sonrasında da 2.sayıyı giriniz:\n(çıkmak için islem numarasına 5 giriniz.\n1-Toplama(+)\n2-Çıkarma(-)\n3-Çarpma(*)\n4-Bölme(/)\n")

cont = True

while cont:

    no1 = int(input("1.sayı: "))
    islem = int(input("Numara: "))
    no2 = int(input("2.sayı: "))

    sonuc=0

    if(islem==1):
        sonuc = no1 + no2
        print(sonuc)
    elif(islem==2):
        sonuc = no1 - no2
        print(sonuc)
    elif(islem==3):
        sonuc = no1 * no2
        print(sonuc)
    elif(islem==4):
        sonuc = no1 / no2
        print(sonuc)
    elif(islem==5):
        cont=False
    else:
        print("geçerli bi işlem girmediniz")