import collections

def checkForWords(mes):
    tempVal = 0
    comWords = open("commonWords.txt")
    while True:
        line = comWords.readline()
        if not line:
            break
        
        line = line.strip()
        if line in mes:
            tempVal = tempVal + mes.count(line)
        
        if tempVal > (len(mes)/4):
            return True

    
    return False
        


def encrypt(mes, key = 10):
    en  = ""

    if f == True:
    
        inputfile = open("textFile2.txt")
        outputfile = open('testFileOutput.txt', 'w')
        while 1:
            char = inputfile.read(1)
            if not char:
                break
            if (ord(char) == 10):
                en += "\n"
            elif (ord(char) == 32):
                en += " "
            else:
                en += chr((ord(char) + key - 33) %95 + 33)
            
            #print((ord(char) + key - 32) %95 + 32)
        
        print(en)
        outputfile.write(en)
        outputfile.close()
        inputfile.close()
 
        
        
    else:
        for i in mes:
            en += chr((ord(i) + key - 33) %95 + 33)
 
    return en


def decryptNoKey(mes):
    i = 0
    mostCommonChars = collections.Counter(mes).most_common(95)

    while i < len(mostCommonChars):
        tempChar = mostCommonChars[i][0]

        guessKey = (ord(tempChar) - 101) 
        if guessKey < 0:
            guessKey = guessKey + 95
        
        #print("guessing key: "+ str(guessKey))
        guessOutput = decrypt(mes, guessKey)
        #print("attempted output: " + guessOutput)
        if (checkForWords(guessOutput) == True) :
            print("Number of keys tried: " + str(i))
            return guessOutput
        i = i +1



def decrypt(mes, tempKey):
    dec = ""
    #if (key == 0):
        #if f == True:
        
    #else:

    
            
        #parse most common words to see if matches
        
        #if neg must add 95
        
        #find most frequent char in encryption
        #find the difference between that value and e
        #decrypt using that key
        

    for i in mes:
        if i == "\n" :
             dec += "\n"
        elif i == " ":
            dec += " "
        else: 
             dec += chr((ord(i) - tempKey-32) %95 + 32)
                
    return dec
   


message = input("Enter the message you want to encode or enter f for a file:\n")

if (message == "f") | (message == "F"):
    f = True
else:
    f = False
key = input("Enter a number as the key:\n")
key = int(key)

if key == 0:
    encryptedMessage = encrypt(message)
else:
    encryptedMessage = encrypt(message, key)


    
if f == False:
    print("encrypted message: " + encryptedMessage)
    if key == 0:
        print("decrypted message (unknown key): " + decryptNoKey(encryptedMessage))
    else:
        print("decrypted message: " + decrypt(encryptedMessage, key))
    
    
else:
    outFile = open("Decrypted.txt", 'w')
    if key == 0:
       outFile.write(decryptNoKey(encryptedMessage))
    else:
        outFile.write(decrypt(encryptedMessage, key))
    outFile.close()


