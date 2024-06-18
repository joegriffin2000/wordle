#wordle dupe
#by joegriffin2000
import random

#loading list of all possible solution words
file = "JoeWordList.txt"
f = open(file,"r")
ListOfWords = f.read().split()
f.close()
ListOfWords.sort()

#loading list of all possible guess words
file = "StanfordWordList.txt"
f = open(file,"r")
AllWordsStanford = f.read().split()
f.close()
AllWordsStanford.sort()

AllLetters = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

#The game loop
def main():
    RandomWord = ListOfWords[random.randint(0,len(ListOfWords))]
    print("Enter a Word! You have 6 Tries.")
    
    user = ""
    counter = 1
    etched = set()
    
    while((user != RandomWord) and (counter <= 6)):
        user = input(" - "+str(counter)+":").strip().lower()
        if (AllWordsStanford.count(user) != 0) and (len(user) == 5):
            print()
            print("\t" + " ".join(list(user)))
            print("\t" + " ".join(getMatchString(RandomWord,user)))
            print()
            
            etched.update(user)
            #print("Tried: "," ".join(etched.difference(set(RandomWord))).upper())
            #print("Available: ", " ".join(AllLetters.difference(etched).union(set(RandomWord))).upper())
            
            counter +=1
        else:
            print("NOT A VALID WORD. TRY AGAIN")
    
    print()
    print("The Word Was:",RandomWord.capitalize())
    
    if (RandomWord == user):
        print("Victory!")
    else:
        print("Too Bad...")

#checking to see which characters match up and which charactsers dont match but appear in the word        
def getMatchString(RandomWord,userWord):
    matchString=["*","*","*","*","*"]
    for i in range(0,len(RandomWord)):
        if RandomWord[i] == userWord[i]:
            matchString[i] = "!"
        elif (RandomWord.count(userWord[i]) > 0):
            matchString[i] = "?"
    
    return matchString

#method for checking for count of a given word
def copyCheck():
    attemptWord = input("word2check: ")
    if (ListOfWords.count(attemptWord) == 1):
        print(True)
    elif (ListOfWords.count(attemptWord) > 1):
        print("ERROR: WORD IS IN THE LIST MORE THAN ONCE ALREADY")   
    else:
        print(False)

#checking to see all plural words that exist in the list of possible solution words     
def printingPlurals():
    for i in ListOfWords:
        if i.startswith("d") and i.endswith('s'):
            print(i)

#getting the total number of words
def wordCount():
    print(len(ListOfWords))

#finding all the words that have a certain ending (has been modified before for certain beginning of words too)
def pieceCheck():
    s1 = 'es'
    for i in ListOfWords:
        if ((i.endswith(s1))):
            print(i)

#Running everything from here. Don't uncomment functions unless debugging
if __name__ == "__main__":
    main()
    #copyCheck()
    #printingPlurals()
    #wordCount()
    #pieceCheck()
    
    input()