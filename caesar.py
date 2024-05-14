import collections
import random

#List of most common chars
letters = [" ","e", "E", "t", "T", "a", "A", "o", "O", "i", "I", "n", "N", "s", "S", "r", "R",
           "h", "H", "d", "D", "l", "L", "u", "U", "c", "C", "m", "M", "f", "F", "y",
           "Y", "w", "W", "g", "G", "p", "P", "b", "B", "v", "V", "k", "K", " x", "X", 
           "q", "Q", "j", "J", "z", "Z"]

#Counts the number of words in the decrypted message that are in a list of Common English Words
def checkForWords(mes):
    tempVal = 0
    comWords = open("commonWords.txt")
    
    #counts the number of words in decrypted message
    numOfWords = mes.count(" ")

    
    while True:
        line = comWords.readline()
        if not line:
            break
        
        line = line.strip()
        tempMes = mes.lower()
        if (" " +line+ " ") in tempMes:
            tempVal = tempVal + tempMes.count(line)
        elif (" " + line) in tempMes:
            tempVal = tempVal + tempMes.count(line)
        elif (line + " ") in tempMes:
            tempVal = tempVal + tempMes.count(line)
        
        #Checks if the number of words in common words is greater than a fourth of the words in the message
        if (tempVal > (numOfWords/4)):
            return True

    return False
        

#Encrypts message with key given, if none provided use default value of 10 (can be anything)
def encrypt(mes, key = random.randint(1,95)):
    en  = ""

    #Checks if we are reading from a file or input
    if f == True:
        inputfile = open("textFile.txt")
        outputfile = open('encryptedFile.txt', 'w')
        while 1:
            char = inputfile.read(1)
            if not char:
                break
            if (ord(char) == 10):
                en += "\n"
                #If you don't want to encrypt spaces, can include the two lines below.
         #   elif (ord(char) == 32):
           #     en += " "
            else:
                en += chr((ord(char) + key - 32) %95 + 32)
            
        outputfile.write(en)
        outputfile.close()
        inputfile.close()
 
        
    #Reading from user input
    else:
        for i in mes:
            en += chr((ord(i) + key - 32) %95 + 32)
 
    return en


#Decrypts message if no key is given
def decryptNoKey(mes):
    i = 0
    j = 0
    #Iterate over all the most common letters
    while (j < len(letters)):
        mostCommonChars = collections.Counter(mes).most_common(95)

        #Iterate over all the most common characters in the encrypted message
        while i < len(mostCommonChars):
            tempChar = mostCommonChars[i][0]

            #Assume most common char is statistically the most common letter
            guessKey = (ord(tempChar) - ord(letters[j])) 
            if guessKey < 0:
                guessKey = guessKey + 95
        
            #print("guessing key: "+ str(guessKey))
            guessOutput = decrypt(mes, guessKey)
            #print("attempted output: " + guessOutput)
            
            #Decrypt message using the guessed key, and check that decrypted file contains verified words
            if (checkForWords(guessOutput) == True) :
                print("Number of keys tried: " +str(i + 1))
                print("Key to Cipher is: "+ str(guessKey))
                return guessOutput
            i = i +1
            
        j = j+1
    #Return false if no key is found: most likely due to a very short message
    return False


#Decrypt given a key
def decrypt(mes, tempKey):
    dec = ""
        
    for i in mes:
        if i == "\n" :
             dec += "\n"
             #Include two lines below if encryption encrypted spaces as well.
       # elif i == " ":
        #    dec += " "
        else: 
             dec += chr((ord(i) - tempKey-32) %95 + 32)
                
    return dec
   


message = input("Enter the message you want to encode or enter f for a file:\n")

if (message == "f") | (message == "F"):
    f = True
else:
    f = False
key = input("Enter a number as the key or enter 0 if you want a random key:\n")
key = int(key)

if key == 0:
    encryptedMessage = encrypt(message)
else:
    encryptedMessage = encrypt(message, key)


#Outputs information to terminal if not a file or to a text file if input was a file.    
if f == False:
    print("encrypted message: " + encryptedMessage)
    if key == 0:
        tempMes = decryptNoKey(encryptedMessage)
        if tempMes != False:
            print("decrypted message (unknown key): " + tempMes )
        else:
            print("Could not decrypt message")
    else:
        print("decrypted message: " + decrypt(encryptedMessage, key))
    
    
else:
    outFile = open("Decrypted.txt", 'w')
    if key == 0:
        tempMes = decryptNoKey(encryptedMessage)
        if tempMes != False:
            outFile.write(tempMes)
        else:
            print("Could not decrypt message")
    else:
        outFile.write(decrypt(encryptedMessage, key))
        
    outFile.close()


