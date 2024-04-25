class Product:
    def __init__(self, nazwa_produktu, czas_produkcji_elementow, zapas, ilosc_produktow_na_wskazany_tydzien, tydzien_na_ktory_chcemy_produkty):
        self.nazwa_produktu = nazwa_produktu
        #self.level = level
        self.czas_produkcji_elementow = czas_produkcji_elementow
        self.zapas = zapas
        self.ilosc_produktow_na_wskazany_tydzien = ilosc_produktow_na_wskazany_tydzien
        self.tydzien_na_ktory_chcemy_produkty = tydzien_na_ktory_chcemy_produkty

class MRP:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_mrp(self):
        for product in self.products:
                print(f"Produkt: {product.nazwa_produktu}")
                for i in range(1, 9):
                    print("Tydzien", i)
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty else product.ilosc_produktow_na_wskazany_tydzien
                    wstepny_zapas = product.zapas if i <= product.tydzien_na_ktory_chcemy_produkty else 0
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    zmontowanie = product.ilosc_produktow_na_wskazany_tydzien - product.zapas if (i == product.tydzien_na_ktory_chcemy_produkty - product.czas_produkcji_elementow) else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty else 0
                    if i > product.tydzien_na_ktory_chcemy_produkty:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")

                print(f"Produkt: Nogi")
                for i in range(1, 9):
                    print("Tydzien", i)
                    zmienna_kurwa_bo_tak = product.zapas #=2
                    potrzeby_brutto = 0 if i < product.tydzien_na_ktory_chcemy_produkty-1 else product.ilosc_produktow_na_wskazany_tydzien*4 - 4*zmienna_kurwa_bo_tak
                    wstepny_zapas = 40 if i <= product.tydzien_na_ktory_chcemy_produkty-1 else 0
                    potrzeby_netto = max(0, potrzeby_brutto - wstepny_zapas)
                    zmontowanie = (product.ilosc_produktow_na_wskazany_tydzien*4 - wstepny_zapas) if i == (product.tydzien_na_ktory_chcemy_produkty-1 - product.czas_produkcji_elementow*2) else 0
                    odbior = potrzeby_netto if i >= product.tydzien_na_ktory_chcemy_produkty-1 else 0
                    if i > product.tydzien_na_ktory_chcemy_produkty-1:
                        potrzeby_brutto = 0
                        wstepny_zapas = 0
                        potrzeby_netto = 0
                        zmontowanie = 0
                        odbior = 0
                    print("Potrzeby brutto:", potrzeby_brutto, "Wstępny zapas:", wstepny_zapas, "Potrzeby netto:", potrzeby_netto, "Wstępne zmontowanie:", zmontowanie, "Zaplanowany odbior:", odbior)
                    print("\n")
if __name__ == "__main__":
    mrp_system = MRP()

    stoly = Product("Stoly", 1, 2, 20, 5)

    mrp_system.add_product(stoly)

    mrp_system.calculate_mrp()

