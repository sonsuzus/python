arkadas = dict()
sayilar = [x for x in range(2,10000,2)]
def bolenler(sayi):
    sinir = sayi//2 + 1
    toplam = 0
    for i in range(1,sinir):
        if sayi%i==0:
            toplam+=i
    return toplam

for x in sayilar:
    z = bolenler(x)
    if x==bolenler(z) and x<z:
        arkadas[x]=z

print(arkadas)
