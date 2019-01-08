#Caesar cipher decryption & encryption script.

import os
import string
import time
import re

alphabetlower = 'abcdefghijklmnopqrstuvwxyz'
alphabetupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Hello, would you like to Encrypt or Decrypt something? ')
print('Press 1 to Encrypt or 2 to Decrypt. ')
choice = True

while choice:
    print('1.Encrypt.')
    print('2.Decrypt.')
    choice = input('What would you like to do? ')
    if choice == '1' :
        filew = input('Enter the path of the text file you want encrypted: ') #user inputs path for the file he wants.
        filex = open(filew)
        print('Key should be between 1-25.') #25 possible ROTs.
        key = int(input('Enter the key: ')) #the number user picks.
        finalenc = ""
        lines = filex.readlines() #read lines
        #print(lines)
        linesstr = ''.join(lines) #list of lines to str
        linesstr = re.sub('[^0-9a-zA-Z]+', '', linesstr) #removes all non alnum chars.
        wordsw = linesstr.split() #read words
        wordslen = [len(i) for i in wordsw]
        #print(wordslen)
        finaldec = ""

        for x in range(len(wordsw)): #loops the lines
            for gg in range(wordslen[x]):
                                            
                character = wordsw[x][gg]
                if (alphabetlower.find(character) >= 0):
                    location = alphabetlower.find(character)
                    new_location = (location - key ) % len(alphabetlower)
                    finaldec += alphabetlower[new_location]
                else:
                    location = alphabetupper.find(character)
                    new_location = (location - key ) % len(alphabetupper)
                    finaldec += alphabetupper[new_location]

        print(finaldec)
        #time.sleep( 0.5 )
        finaldec = ""
        break

    elif choice == '2':
            ocrh = input('Enter the path of the text file you want decrypted: ') #user inputs path for the file he wants.
            ocr = open(ocrh)

            lines = ocr.readlines() #read lines
            #print(lines)
            linesstr = ''.join(lines) #list of lines to str
            linesstr = re.sub('[^0-9a-zA-Z ]+', '', linesstr) #removes all non alnum chars.
            wordsw = linesstr.split() #read words
            wordslen = [len(i) for i in wordsw]
            #print(wordslen)
            finaldec = ""


            for x in range(len(wordsw)): #loops the lines
                
                for j in range(25): #26 times for all possible letter swaps.
                    
                    for gg in range(wordslen[x]):
                                
                        character = wordsw[x][gg]
                        

                        if (alphabetlower.find(character) >= 0):
                            location = alphabetlower.find(character)
                            new_location = (location - j + 1 ) % len(alphabetlower)
                            finaldec += alphabetlower[new_location]
                        else:
                            location = alphabetupper.find(character)
                            new_location = (location - j + 1 ) % len(alphabetupper)
                            finaldec += alphabetupper[new_location]
            
                    print(finaldec)
                    #time.sleep( 0.5 )
                    finaldec = ""
                ocr.close()
            break
    else:
        print('Invalid input, you have to select between 1(Encrypt) or 2(Decrypt)!')
