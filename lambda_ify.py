wiek = lambda wiek: "dziecko" if wiek < 12 else ("Nastolatek" if wiek < 18 else "Dorosły")
print(wiek(15))
print(wiek(10))
print(wiek(25))