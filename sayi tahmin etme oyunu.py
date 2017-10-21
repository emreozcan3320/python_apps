# -*- coding: utf-8 -*-
from random import randint

def main():
    print("\n ### Merhaba sayi bulma oyununa hos geldiniz \n ### 1 ile 100 arasinda bir sayi olusturucaz\n ### bunu tahmin etmeye calisin")
    print("-------------------------------------------------------------")
    a = randint(0, 100)
    print(a)
    try:
        tahmin = int(input("\n-Bir sayi tahmin et :D \n "))
        while True:
            if tahmin > a :
                tahmin = int(input("--Kucuk bir sayi tahmin et :D \n-> "))
            elif tahmin < a :
                tahmin = int(input("--Buyuk bir sayi tahmin et :D \n-> "))
            elif tahmin == a :
                print("\n-- EVREKAA BULDUN BRO --")
                print("-------------------------------------------------------------")
                break
        while True:
            cevap = input("\n--tekrar oynamak ister misin ? E / H \n")
            print(cevap)
            cevap = cevap.lower()
            if cevap == "e" or cevap == "evet":
                main()
            elif cevap == "h" or cevap == "hayir":
                print("\n--Hoscakal :S")
                break
            else:
                print("\n--Lutfen dogru bir cevap giriniz")
                
    except ValueError:
        print("\n--lutfen bir saiı gir")
        main()

if __name__ == "__main__":
    main()
