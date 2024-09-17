invoer1 = input("Hoe ver rij je iedere dag?")
invoer2 = input("Geef de afstand in kilometer in.")
afstand = int(invoer2)
gecorrigeerdeafstand = afstand - 1
rit = int(invoer1)
dagen = (gecorrigeerdeafstand // rit) + 1
afdruk = "Je komt op dag " + str(dagen) + " aan op jouw bestemming."
print(afdruk)