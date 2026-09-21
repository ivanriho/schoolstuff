"""fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)"""

"""for i in range(6):
    print("Hello")"""

"""for i in range(12, 0, -2):
    print(i)"""

"""word = "pytzeezthon"
for letter in word:
    print("e3")"""

count = 0
while count < 5:
    print(count)
    count += 1 

password = "" # Skapar en variabeln med tomt värde waiting difiniton
while password != "password123": # Loopen körs sålänge != inte är password123
    password = input("Please enter the password: ") # Input gör att password blir defined
    if password == "quit": # Om lösenordet är quit så -
        break # - så avbryts hela loopen
    print("Incorrect password!") #Outputa fel lösenord och inte skrev quit
print("Welcome!") #Denna rad har INGET indrag. Den ligger UTANFÖR loopen!
