for sayi in range(2,1000):
    asal = True
    for bolen in range(2,sayi):
        if sayi%bolen==0:
            asal = False
    if asal:
        print(sayi, end = "-")
