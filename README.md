Caesar Cipher on user input and text file. Can alter the contents of testFile.txt for different messages to encrypt, or enter into terminal when prompted.
To see decryption algorithm make use of statistical analysis and letter frequency, enter a key of 0, for a random encryption.


**Advantages of the decryption alogrithm with unknown key:**

Program finds the correct key within 1 attempt if spaces are encrypted.

Program finds the correct key on averarge within 5 attempts if spaces aren't encrypted.


**Limitations for breaking the encryption (unknown key):**

Very short messages, such as one word, will fail to decrypt.

No spaces in the message will also fail, as the program tests for spaces before and after words to ensure it wasn't a random chance of a short word appearing
in the decryption. For example: dXd#usHd ("us" appears by chance, but doesn't make sense). 

Program also counts number of words that correctly appear in decryption to prevent previous example for occuring, but with spaces, 
which can cause failure on very unique text files with heavy word jargon not commonly used. This could be resolved by decreasing the ratio of common words
that must be within the decrypted file to allow it to pass, or increasing the size of the dictionary of common words.
