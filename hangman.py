import random

file = open("word.txt", "r")
lWordList = file.readlines
lwordList1 = []
for line in lWordList:
        number = 0
        while number < 5:
            lWordList1.append(str(item)+str(number))
            number = number + 1
            print (lWordList1)
# lWordList = ["able", "about","account","acid","across","act","addition","adjustment"]
random.shuffle(lWordList)

sRealWord = lWordList[0].upper()
print(sRealWord)
 
lShownWord = "_ " * len(sRealWord)

print(lShownWord)

iAllowedGuesses = 10
iRightGuesses = 0
sInput = ""

while True:

    if(sInput == "END"):
        break

    
    print("Guesses left: {}".format(iAllowedGuesses))
    print("The word you are looking for is: " + str(lShownWord) )
    sInput = input("Enter letter: ").upper()
    
    if len(sInput) != 1:
        print("your guesses should be of 1 alphabet.")
        continue

    if lShownWord.count(sInput) != 0:
        print("You have already guessed this word")
        continue
        
    bIsGuessHit = False
    iLetterNumber = 0
    
    while iLetterNumber < len(sRealWord):
        if(sRealWord[iLetterNumber] == sInput):
            lShownWordList = list(lShownWord.replace(" ", ""))
            lShownWordList[iLetterNumber] = sInput
            lShownWord = " ".join(lShownWordList)
            bIsGuessHit = True
            iRightGuesses += 1
        iLetterNumber += 1

    if not bIsGuessHit:
        iAllowedGuesses -= 1
    
    if iAllowedGuesses == 0:
        print("You are out of guesses. You are Hanged.")
        break

    if iRightGuesses == len(lShownWord.replace(" ", "")):
        print(str(lShownWord).replace(" ", ""))
        print("you have won")
        break
