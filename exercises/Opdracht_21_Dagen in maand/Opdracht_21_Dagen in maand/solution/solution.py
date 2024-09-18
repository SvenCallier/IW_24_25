inp = input("Geef de maand in.")
maand = int(inp)

if maand == 2:
    dagen = 28
elif maand == 4 or maand == 6 or maand == 9 or maand == 11:
    dagen = 30
else:
    dagen = 31

print(dagen)