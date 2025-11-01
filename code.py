import random
listofNumbers = []

while True:
    inp = input("Would you like to add a new number (y)?    ")
    if inp == "y":
        try:
            targetVal = int(input("Enter the new integer:   "))
            listofNumbers.append(targetVal)
            print()
            print("--------")
        except ValueError:
            print("Invalid input!")
            print()
            print("--------")
    else:
        break
  
newNumber = 0 
for i in listofNumbers: 
     newNumber += i 
     
print(f"Result: {newNumber}")