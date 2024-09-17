invoer = input("Geef een getal in.")
getal = float(invoer)
getal = getal * 10
resultaat = int(getal % 10)
afdruk = '"' + str(resultaat) + '" is het eerste decimale cijfer van het getal.'
print(afdruk)