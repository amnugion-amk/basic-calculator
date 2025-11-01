import random

# -- List of numbers that will be processed 
listofNumbers = [3, 4, 5] 

# -- Runs a random amount of times, from 1 to 1000
for i in range(1, random.randint(1, 100+1)): 
    
     # -- Picks a number from 1 to 1000 and stores it
    newRandomInt = random.randint(1, 1000)
    
    # -- Appends the new number to the list of to-be processed numbers
    listofNumbers.append(newRandomInt) 

# -- Initializes the final unprocessed product as 1
newNumber = 0 

# -- Runs through each number in the to-be processed numbers list
for i in listofNumbers: 
    
    # -- Adds the to-be processed number to the final product
    newNumber += i 
    
# -- Prints the final product
print("Here is the new number: "+str(newNumber)) 