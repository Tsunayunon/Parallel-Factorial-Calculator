import multiprocessing

def faktoriyel_hesapla(sayi):
    carpim = 1
    for i in range(1, sayi + 1):
        carpim *= i
    return f"{sayi} sayısının faktoriyeli {carpim} dir"

def ana_fonksiyon():
    sayilar = range(1, 101) 
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as havuz:
        sonuclar = havuz.map(faktoriyel_hesapla, sayilar)
        for sonuc in sonuclar:
            print(sonuc)



if __name__ == "__main__":
    ana_fonksiyon()
