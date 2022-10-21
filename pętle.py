# warunek = 't'
#
# while warunek == 't':
#     sales = float(input("podaj wielkość sprzedaży: "))
#     rate = float(input("podaj wysokość premii: "))
#
#     wynik = sales * rate
#
#     print("-" * 20)
#     print("Premia wynosi:", format(wynik, ' .2f'), ' zł', sep='') # sep = separator. Można tutaj wstawić dowolny znak
#     print("-" * 20)
#     warunek = input("Czy chcesz obliczyć kolejną premię? (t lub n): ")
#
# print("To jest poza pętlą!!!")

# print("MENU:")
# warunek = input("Wpisz 't' aby rozpocząć liczenie premii.")
#
# while warunek == 't':
#     sales = float(input("podaj wielkość sprzedaży: "))
#     rate = float(input("podaj wysokość premii: "))
#
#     wynik = sales * rate
#
#     print("-" * 20)
#     print("Premia wynosi:", format(wynik, ' .2f'), ' zł', sep='') # sep = separator. Można tutaj wstawić dowolny znak
#     print("-" * 20)
#     warunek = input("Czy chcesz obliczyć kolejną premię? (t lub n): ")
#
# print("To jest poza pętlą!!!")

# licznik = 0
# while True:
#     licznik += 1 # licznik = licznik + 1. Można tutaj również przy tym zapisie odejmować, mnożyć itd.
#     print(licznik)
#     if licznik == 2:
#         break

# wybor = int(input("Ile razy mam wykonać ksero?"))
# for i in range(wybor): # zamiast i można sobie tutaj wpisać dowolny tekst jaki nas interesuje
#     print(i+1) #jezeli nie chcemy, by w princie zaczynało się odliczanie od 0
#     print("Robię ksero...")
import random

# lista = []
# ilosc = random.randint(3, 8)
# for i in range(ilosc):
#     lista.append(random.randint(1, 10))
# # for i in lista:
# # #     print(f"elementy w liście: {i}")
#
# for i, w in enumerate(lista):
#     print(f"indeks: {i}, elementy w liście: {w}")
#
# slownik = {"imię": "Marek", "nazwisko": "Kowalski", "płeć": "Mężczyzna"}
# for k, w in slownik.items():
#     # print(k)
#     print(w)

# lista = []
# ilosc = random.randint(3, 8)
# for i in range(ilosc):
#     lista.append(random.randint(1, 10))
# # for i in lista:
# # #     print(f"elementy w liście: {i}")
# krotka = ()
#
# for i, w in enumerate(lista):
#     print(f"indeks: {i}, elementy w liście: {w}")
#     if w == 10:
#         print("Znalazłem 10!!!")
#         krotka += w,
# print(krotka)


lista = []
ilosc = random.randint(3, 8)
for i in range(ilosc):
    lista.append(random.randint(1, 10))
# for i in lista:
# #     print(f"elementy w liście: {i}")
krotka = ()

for i, w in enumerate(lista):
    print(f"indeks: {i}, elementy w liście: {w}")
    if w == 10:
        print("Znalazłem 10!!!")
        krotka += w,
        liczba1 = krotka[0]
        print(f"Dodajemy +5 do wartości krotki {liczba1 + 5}")