'''
Algorytm MRP dla produkcji stołów z podziałem na poziom 0, 1 i 2. 
Cała produkcja zajmuje minimalnie 9 tygodni, przy założeniu, że stoły wytwarzane są 1 tydzień.
Nogi i płyta pilśniowa wytwarzane są z reguły 2 razy dłużej.
Blaty i listwa wykończeniowa wytwarzane są 3 razy dłużej.
Możemy samodzielnie określić zapas stołów, nóg i blatów w magazynie.
Możemy również określić, ile stołów chcemy i na jaki tydzień. 
'''


class Product:
    def __init__(self, czas_produkcji_elementow, zapas_stolow, zapas_nog, zapas_blatow, ilosc_produktow_na_wskazany_tydzien, tydzien_na_ktory_chcemy_produkty):
        self.czas_produkcji_elementow = czas_produkcji_elementow
        self.zapas_stolow = zapas_stolow
        self.zapas_nog = zapas_nog
        self.zapas_blatow = zapas_blatow
        self.ilosc_produktow_na_wskazany_tydzien = ilosc_produktow_na_wskazany_tydzien
        self.tydzien_na_ktory_chcemy_produkty = tydzien_na_ktory_chcemy_produkty

class MRP:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_mrp(self, ilosc_tygodni):

        for product in self.products:
                print("Produkt: Stoły")
                for i in range(1, ilosc_tygodni + 1):
                    print("Tydzien", i)
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty else product.ilosc_produktow_na_wskazany_tydzien
                    wstepny_zapas = product.zapas_stolow if i <= product.tydzien_na_ktory_chcemy_produkty else 0
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    a = product.ilosc_produktow_na_wskazany_tydzien - product.zapas_stolow
                    zmontowanie = a if (i == product.tydzien_na_ktory_chcemy_produkty - product.czas_produkcji_elementow) and a > 0 else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty else 0
                    if i > product.tydzien_na_ktory_chcemy_produkty:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                        a = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")

                print("Produkt: Nogi")
                for i in range(1, ilosc_tygodni + 1):
                    print("Tydzien", i)
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty-1 else product.ilosc_produktow_na_wskazany_tydzien*4 - product.zapas_stolow*4
                    wstepny_zapas = product.zapas_nog if i <= product.tydzien_na_ktory_chcemy_produkty-1 else 0
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    a = (product.ilosc_produktow_na_wskazany_tydzien*4 - product.zapas_stolow * 4 - product.zapas_nog)
                    zmontowanie = a if i == (product.tydzien_na_ktory_chcemy_produkty-1 - product.czas_produkcji_elementow*2) and a > 0 else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty-1 else 0
                    if i >= product.tydzien_na_ktory_chcemy_produkty:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                        a = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")

                print("Produkt: Blaty")
                for i in range(1, ilosc_tygodni + 1):
                    print("Tydzien", i)
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty-1 else product.ilosc_produktow_na_wskazany_tydzien - product.zapas_stolow
                    wstepny_zapas = product.zapas_blatow if i <= product.tydzien_na_ktory_chcemy_produkty-1 else 0
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    a = product.ilosc_produktow_na_wskazany_tydzien - product.zapas_blatow - product.zapas_stolow
                    zmontowanie = a if (i == product.tydzien_na_ktory_chcemy_produkty-1 - product.czas_produkcji_elementow*3) and a > 0 else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty-1 else 0
                    if i > product.tydzien_na_ktory_chcemy_produkty-1:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                        a = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")

                print("Produkt: Płyta pilśniowa")
                for i in range(1, ilosc_tygodni + 1):
                    print("Tydzien", i)
                    a = product.ilosc_produktow_na_wskazany_tydzien - product.zapas_blatow - product.zapas_stolow
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3 or a < 0 else a
                    wstepny_zapas = 0 
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    zmontowanie = a if (i == product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3 - product.czas_produkcji_elementow*2) and a > 0 else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3 else 0
                    if i > product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                        a = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")
                    

                print("Produkt: Listwa wykończeniowa")
                for i in range(1, ilosc_tygodni + 1):
                    print("Tydzien", i)
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3 else product.ilosc_produktow_na_wskazany_tydzien*3 - product.zapas_blatow*3 - product.zapas_stolow*3
                    wstepny_zapas = 0 
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    a = product.ilosc_produktow_na_wskazany_tydzien*3 - product.zapas_blatow*3 - product.zapas_stolow*3
                    zmontowanie = a if (i == product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3 - product.czas_produkcji_elementow*3) and a > 0 else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3 else 0
                    if i > product.tydzien_na_ktory_chcemy_produkty-2 - product.czas_produkcji_elementow*3:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                        a = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")
                

if __name__ == "__main__":
    mrp_system = MRP()

    try:
        czas_produkcji_elementow = int(input("Podaj czas produkcji stołów(w tygodniach):"))
        ilosc_tygodni_minimalnie = czas_produkcji_elementow * 3 + czas_produkcji_elementow * 3 + 3
        print("Uwaga! Minimalna liczba tygodni potrzebna do produkcji na wszystkich poziomach:", ilosc_tygodni_minimalnie)
        ilosc_tygodni = int(input("Podaj ilość tygodni, dla których wyświetlić algorytm: "))
        zapas_stolow = int(input("Podaj ilość zapasów stołów: "))
        zapas_nog = int(input("Podaj ilość zapasów nóg: "))
        zapas_blatow = int(input("Podaj ilość zapasów blatów: "))
        ilosc_produktow_na_wskazany_tydzien = int(input("Podaj ilość produktów na wskazany tydzień: "))
        tydzien_na_ktory_chcemy_produkty = int(input(f"Podaj tydzień, na który jest zamówienie (Uwaga! Czas produkcji to minimalnie {ilosc_tygodni_minimalnie}: )"))

        stoly = Product(czas_produkcji_elementow, zapas_stolow, zapas_nog, zapas_blatow, ilosc_produktow_na_wskazany_tydzien, tydzien_na_ktory_chcemy_produkty)
        # 1, 2, 20, 4, 20, 9
        mrp_system.add_product(stoly)
        mrp_system.calculate_mrp(ilosc_tygodni)
        
    except ValueError:
        print("Błąd: Podana wartość nie jest liczbą całkowitą.")
