def parseFirstLetter(userInput):
    firstLetterUpperCase = userInput[0].upper()
    return firstLetterUpperCase
    
userInput = input()
parsedUserInput = parseFirstLetter(userInput)
print("Tell me your password: " + parsedUserInput)