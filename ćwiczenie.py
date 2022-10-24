dni_tyg = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
Dni_pobrane = dni_tyg[2:6]
print(f"Wybrane dni z listy: {Dni_pobrane}")

for i in dni_tyg[2:6]:
    print(i)


dni_pobrane = []
for i, w in enumerate(dni_tyg):
    if i> 1 and i <7:
        dni_pobrane.append(w)

print(dni_pobrane)
