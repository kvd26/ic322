#Part 1 of Lab 01
#Kaj Dongre 
#261650

numbers = []

#read in a text file with one number per line

with open("numbers.txt", "r") as file:
    for line in file:
        numbers.append(float(line))

numbers.sort() #sort numbers in ascending order 

#print numbers one per line 
for number in numbers:
    print(number)