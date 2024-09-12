ih1=input("Geef het uur van tijdstip 1.")
im1=input("Geef het aantal minuten van tijdstip 1.")
is1=input("Geef het aantal seconden van tijdstip 1.")
ih2=input("Geef het uur van tijdstip 2.")
im2=input("Geef het aantal minuten van tijdstip 2.")
is2=input("Geef het aantal seconden van tijdstip 2.")

h1=int(ih1)
m1=int(im1)
s1=int(is1)
h2=int(ih2)
m2=int(im2)
s2=int(is2)

tijd2 = s2 + (60 * m2) + (60 * 60 * h2)
tijd1 = s1 + (60 * m1) + (60 * 60 * h1)

verschil = tijd2 - tijd1

print("Er liggen",verschil,"seconden tussen beide tijdstippen.")