import googletrans
from googletrans import Translator
import csv
import re
import language_tool_python

    
print("Welcome to Indo slang to English Translator")
print("Do not use any void characters in continuation")

print('===================================================')

trans = Translator()
tool = language_tool_python.LanguageTool('en-US')
def translator(user_string):
    user_string = user_string.split(" ")
    a = 0
    for string in user_string:
        # File path which consists of Abbreviations.
        fileName = "slang.txt"
        # File Access mode [Read Mode]
        accessMode = "r"
        with open(fileName, accessMode) as slang:
            # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
            dataFromFile = csv.reader(slang, delimiter="=")
            # Removing Special Characters.
            string = re.sub('[^a-zA-Z0-9-_.]', '', string)
            for row in dataFromFile:
                # Check if selected word matches short forms[LHS] in text file.
                if string.upper() == row[0]:
                    # If match found replace it with its appropriate phrase in text file.
                    user_string[a] = row[1]
            slang.close()
        a = a + 1
    # Replacing commas with spaces for final output.
    y = ' '.join(user_string)
    z = tool.correct(y)
    if x == y:
     print('===================================================')
     print('NO SLANG FOUND!!!')
    print('===================================================')
    print('Grammar not fixed:')
    print(y)
    print('')
    print('Fixed grammar:')
    print(z)
    print('===================================================')
    if y == z:
     print('NO GRAMMATICAL ERROR!!!')
    print('')

while True:
    print("Input a sentence below or print exit to end script")
    # Getting User String.
    # Sample : input = " gasss sekarang!"
    userInput = input()
    # Keep Calling procedure until EXIT or exit keyword is encountered.
    if userInput.upper() == 'EXIT':
        print("Exiting Script")
        break
    myTranslate = trans.translate(userInput, dest='en')
    x = myTranslate.text
    translator(x)