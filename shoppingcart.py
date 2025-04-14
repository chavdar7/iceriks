print("!!!Mağazamıza hoşgeldiniz!!!")
print("*****************************\n")

things = ["Elma(kg)", "Domates(kg)", "Çay(pkt)", "Kahve(pkt)"]
prices = [10, 15, 100, 120]

print("Fiyatlar")
for i in range(len(things)):
    print(f"{things[i]:<12} {prices[i]:>3}₺")

print("\n")

sepet = 0

while True:
    istek = input("Ne almak istiyorsunuz(E, D, Ç, K)(Çıkmak için q): ")
    istek = istek.upper()
    adet = int(input("Kaç kg veya adet almak istiyorsunuz: "))

    if istek == "E":
        sepet += prices[0]*adet
    elif istek == "D":
        sepet += prices[1]*adet
    elif istek == "Ç":
        sepet += prices[2]*adet
    elif istek == "K":
        sepet += prices[3]*adet
    elif istek == "q" or istek == "Q":
        break
    else:
        print("geçerli harf veya adet girmediniz")

    print(f"Şuanki sepet tutarınız: {sepet}")

print(f"Son sepet tutarınız: {sepet}")

