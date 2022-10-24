def policz(a, b):
    suma = a + b
    return suma


# suma = policz(5, 4)
# print(suma)
# suma2 = policz(9, 9)

suma3 = lambda a, b: a + b

print(suma3(3, 4))
print((lambda a, b: a + b)(3, 4))
wynik = (lambda a, b: a + b)(3, 4)
print(wynik)

# print(suma + 10)
# print(suma2 + suma)