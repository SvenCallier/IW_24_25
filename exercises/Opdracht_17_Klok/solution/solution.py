invoer1=input("Geef het aantal voor de klas in lokaal 101.")
invoer2=input("Geef het aantal voor de klas in lokaal 102.")
invoer3=input("Geef het aantal voor de klas in lokaal 103.")
klasA=int(invoer1)
klasB=int(invoer2)
klasC=int(invoer3)

bankA= klasA//2 + klasA%2
bankB= klasB//2 + klasB%2
bankC= klasC//2 + klasC%2

banken = bankA + bankB + bankC

print("Er moeten", banken, "banken worden aangekocht.")