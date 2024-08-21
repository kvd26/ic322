#Part 2 of Lab 1
#Kaj Dongre
#261650

#create a dictionary of words
wordCount = {}

with open("words.txt", "r") as file:
    for line in file:
        for word in line.split():
           #if word does exist in wordCount, add 1 to its definition
            if word.lower() in wordCount:
                wordCount[word.lower()] += 1
            #if word does not exist in wordCount, add it, and make the def = 1

            else:
                wordCount[word.lower()] = 1

#sort wordCount based on the values 
sortedWordCount = sorted(wordCount.items(), key=lambda x:x[1], reverse = True)

#print out the 5 most commonly used words
for i in range(5):
    print(sortedWordCount[i][0] + ": " + str(sortedWordCount[i][1]))
    