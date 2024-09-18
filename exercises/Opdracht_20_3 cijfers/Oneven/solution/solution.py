inv = input("Geef een getal in.")
getal = int(inv)

if getal < 1000 and getal > 99:
    afdruk = "Het getal bestaat uit 3 cijfers."
else:
    afdruk = "Het getal bestaat niet uit 3 cijfers."
    
print(afdruk)