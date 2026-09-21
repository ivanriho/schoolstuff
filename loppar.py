"""
------------------------------
## Kod 1: Fruktlistan 🍎🍌🍒

fruits = ["apple", "banana", "cherry"]for fruit in fruits:
    print(fruit)


* Vad den gör: Du har en korg med tre frukter. Loopen plockar upp en frukt i taget, tittar på den och skriver ut namnet på skärmen.
* Vad som visas på skärmen:

apple
banana
cherry


------------------------------
## Kod 2: Tjat-maskinen 🗣️

for i in range(6):
    print("Hello")


* Vad den gör: range(6) betyder bara "gör detta 6 gånger". Loopen är som en person som säger "Hello", tar ett streck i luften, och upprepar det tills den har gjort det 6 gånger.
* What som visas på skärmen: Ordet "Hello" skrivs ut på sex rader.

Hello
Hello
Hello
Hello
Hello
Hello


------------------------------
## Kod 3: Nedräkningen (Backa i kön) 📉

for i in range(12, 0, -2):
    print(i)


* Vad den gör: range(starta_på, stoppa_innan, hur_många_steg_vi_backar).
Här säger du till datorn: "Starta på 12. Räkna bakåt. Ta bort 2 för varje steg. Stoppa innan du når 0."
* Vad som visas på skärmen:

12
10
8
6
4
2


------------------------------
## Kod 4: Det "hemliga" ordet 🕵️‍♂️

word = "pytzeezthon"for letter in word:
    print("e3")


* Vad den gör: Det här är en luring! Loopen går igenom ordet "pytzeezthon" bokstav för bokstav. Ordet har 11 bokstäver, så loopen kommer att snurra 11 gånger.
Men istället för att skriva ut bokstaven, tvingar vi datorn att skriva ut texten "e3" på varje varv!
* Vad som visas på skärmen: Texten "e3" skrivs ut 11 gånger på rad (eftersom ordet har 11 bokstäver).

e3
e3
(och så vidare, totalt 11 gånger...)


------------------------------
## Kod 5: Den gamla vanliga räknaren (While) 🔢

count = 0while count < 5:
    print(count)
    count += 1


* Vad den gör: Det här är precis samma sak som vi gjorde med din multiplikationstabell!
* count = 0 är vår startlåda.
   * while count < 5 betyder "snurra så länge det är mindre än 5".
   * count += 1 är bara ett kortare sätt att skriva count = count + 1 (vår lådflyttning!).
* Vad som visas på skärmen: Den skriver ut numret i lådan, och plussar på 1, tills den når 5.

0
1
2
3
4


Vilken av de här fem koderna känns krångligast att förstå, eller vill du att vi ändrar på någon av dem för att testa vad som händer?

"""