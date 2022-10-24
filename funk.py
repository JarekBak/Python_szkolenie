import random

a = random.randint(1, 100)
b = random.randint(1, 100)
x = int(input("Podaj liczbę x: "))


def dodaj():
    global b
    a = int(input("Podaj a "))
    b = int(input("Podaj b "))
    print("Suma =", a + b)


def odejmij(a, b):
    print(f"Liczba a={a}, liczba b={b}")
    print("Wynik odejmowania =", a - b)


def pomnoz(a, x=1):
    # x = 1000
    print(f"Liczba a={a}, liczba x={x}")
    print("Wynik mnożeniea =", a * x)


def podziel():
    pass


def suma(*param):
    print(param)

##################################################################################################

while True:
    print('''
       *** MENU ***
        1. dodaj
        2. odejmij
        3. pomnóż
        4. podziel(chwilowo nieczynne) 
        5. koniec
        t = test sumy
        ''')
    w = input("Mój wybór: ")
    if w == "1":
        dodaj()
    elif w == "2":
        odejmij(a, b)
    elif w == "3":
        pomnoz(a, x)
    elif w == "4":
        podziel()
    elif w == "5":
        break
    elif w == "t":
        lista = []
        while True:
            wejscie = input()
            if wejscie == "stop":
                break
            lista.append(int(wejscie))
            for i in lista:
                suma(i)
        print("Suma podanych parametrów to:", sum(lista))
    else:
        print("Nie ma takiej opcji, spróbuj ponownie")