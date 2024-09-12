invoer = input ("Geef een getal in.")
getal = int(invoer)
honderdtallen = getal // 100
get100 = getal - (honderdtallen*100)
eenheden = getal % 10
tientallentussenstap = getal // 10
tientallen = tientallentussenstap % 10
resultaat = str(honderdtallen) + str(eenheden) + str(tientallen)
print(resultaat)