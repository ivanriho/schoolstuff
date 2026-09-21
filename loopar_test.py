# SÅ HÄR GÖR MAN I VERKLIGHETEN (Utan if):
tal = int(input("Vilken multiplikationstabell vill du se? "))
räknare = 1

while räknare <= 14:
    print(räknare, "*", tal, "=", räknare * tal)
    räknare = räknare + 1
