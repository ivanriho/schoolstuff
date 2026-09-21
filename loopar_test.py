import sys
# SÅ HÄR GÖR MAN I VERKLIGHETEN (Utan if):
tal = int(input("Vilken multiplikationstabell vill du se? "))
räknare = 1

if tal == int(3):
    print("Erm nej tack")
    sys.quit()
while räknare <= 14:
    print(räknare, "*", tal, "=", räknare * tal)
    räknare = räknare + 2
