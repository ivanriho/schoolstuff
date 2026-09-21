#kommentarer, if, {}, kommatecken"
#ska göra en kassörs
import time
import sys

# The menu with all the different alternatives and prices
plainPizza = int(80)
Margarita = plainPizza + 20 # 100 kr
Vesuvio = plainPizza + 40
Menu = [Margarita, Vesuvio]
order_number = Vesuvio 

# Welcomes and asks for which pizza you'd like
print("Välkommen till våran resturang")
order = input("Vad skulle du vela beställa? ").casefold()
order_price = int(order_number)

#Göra olika storlekar på pizzan
size = input("Vilken storlek vill du ha på pizzan, vi har small, medium och large!")
if "small" in size:
    order = order
elif "medium" in size:
    order + (20)
elif "large" in size:
    order + int(35)


# Saying good choice and asking when you'd want it
# cookingTime will the be time varible that later will be used to display the time in the string

print("Bra val")
cookingTime = input("Om hur lång tid vill du ha den? ")
print("Perfekt det passar oss båda, då kommer den om", cookingTime, "min")

# Add-ons that both Margarita and Vesuvio can use, it'll ask you, depening on the choice sås will be offered as an alternative

ost = int(10)
oliver = int(15)
banan = int(25)
svamp = int(17)
sås = int(12)
    
# Depending on the pizza, the output will choose between the text without Sauce and the one with Sauce 

if order == "vesuvio":
    extra =input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. För denna har vi även sås! ")
elif order == "margarita":
    extra = input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. ")


print("Tack för din beställning, vi kommer att börja laga den nu, ge oss några sekunder att sätta in ordern")

time.sleep(5)

if order == "vesuvio":
    totalSum = Vesuvio
else: 
    totalSum = Margarita

#Will add the price of the add-ons to the pizzas total price, instead of using specific words to enter add on you can write anything you'd like 
#Because it searches for the word inside!

if "ost" in extra:
    totalSum += ost

if "oliver" in extra:
    totalSum += oliver

if "banan" in extra:
    totalSum += banan

if "svamp" in extra:
    totalSum += svamp

if "sås" in extra:
    totalSum += sås

# Adding the drinking questions now

cola = int(20)
sprite = int(15)
fanta = int(25)


drinks = input("Vill du ha nått att dricka till? Vi har cola, fanta och sprite. ")

if "cola" in drinks:
    totalSum += cola
if "fanta" in drinks:
    totalSum += fanta
if "sprite" in drinks:
    totalSum += sprite


#Announcing the price 
# Setting tip variable
# Making sure you can't tip negative

x = int(40)
y = int(0)
print(f"Priset blir", totalSum, "kr exlusive dricks, med din order som var en", order, "med", drinks,)

answer = input("Vill du ge dricks till lilla mig?")

if "nej" in answer:
    print("Fahhh ig vro")

elif "ja" in answer:
    print("tack så mycket")

    resultat = input("Hur mycket merci ")
    resultat = int(resultat)

    if resultat >= 40:
        print("Tack så mycket för att du dricksar med dina stora", resultat, "spänn, du får snart sätta dig!")

    elif resultat < 40:
        print("Det är väl omtanken som räknas ig, tack för dina", resultat, "spänn, snart får du sätta dig om du vill")

    


time.sleep(15)

sittingDown = input("Vill du fortfarande sätta dig ner och vänta på din pizza? ")
if "ja" in sittingDown:
    print("Perfekt, då får du sätta dig ner och vänta på din pizza, den kommer snart!")
    time.sleep(10)
    print("Här är din pizza! Ha en bra dag!")
    sys.exit()
if "nej" in sittingDown:
    print("Oh det är väl okej ig, den kommer snart")
    time.sleep(5)
    print("Här, ses någon annan gång")
    sys.exit()
    
""" En sammanfattning av programmet är att det är en enkel kassörsprogram som tar emot beställningar 
    för pizza och dryck, beräknar totalpriset inklusive eventuella tillägg och dricks, och ger 
    användaren möjlighet att sitta ner och vänta på sin beställning. 
    Programmet använder sig av if-satser för att hantera olika val och inmatningar från användaren.



int = 3
float = 3.0
str = "3"
You can get the type of a varible by using type() ex= print(type(x))
A and a is different varibles, it's case sensitive
"""