import random
listofNumbers = [3, 4, 5] 

for i in range(1, random.randint(1, 100+1)): 
    newRandomInt = random.randint(1, 1000)
    listofNumbers.append(newRandomInt) 
    
newNumber = 0 
for i in listofNumbers: 
     newNumber += i 
     
print("here you idiot who is too lazy to count: "+str(newNumber)) 