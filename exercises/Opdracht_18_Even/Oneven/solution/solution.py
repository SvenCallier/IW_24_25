invoer = input("Geef de stand van de kleine wijzer in.")
standkw = int(invoer)
deeluur = standkw%30 / 30
standgwF = deeluur*360
standgwD = int(standgwF)
minF = standgwF / 6
minD = int(minF)
afdruk1 = "De grote wijzer is dit uur al "+ str(standgwD) + "° gedraaid."
afdruk2 = "Er zijn " + str(minD) + " minuten voorbij."
print(afdruk1)
print(afdruk2)