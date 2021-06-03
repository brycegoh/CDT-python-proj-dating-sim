'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game

Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''

# This function takes in  a STRING and returns the user's input as a INT.
def integerInput(inputString):
    if type(inputString) is str :
        try: return int( input(inputString) )
        except ValueError: 
            print("Incorrect input")
            return integerInput(inputString)
    else:
        raise ValueError("Please ensure function input is a String.")

# This function takes in  a STRING and returns the user's input as a FLOAT.
def floatInput(inputString):
    if type(inputString) is str :
        try: 
            return float( input(inputString) )
        except ValueError: 
            print("Incorrect input")
            return floatInput(inputString)
    else:
        raise ValueError("Please ensure function input is a String.")

# This function checks if the String input is of
# 1. length of between 7 to 14 characters excluding any spaces
# 2. At least 2 numbers
# 3. No spaces
# 4. No special characters
# It will then print an error message if there is any
# It will then return True or False if the name is ok or not.

def validateString(userInput):
    userInput = userInput.strip() #This removes starting and ending spaces
    listOfNumbers = [alphabet for alphabet in userInput if alphabet.isdigit()]
    rules = [
        " " not in userInput,
        len(userInput) >= 7,
        len(userInput) <= 14,
        len(listOfNumbers) >= 2,
        userInput.isalnum()
    ]
    if  all(rules):
        return True
    else:
        counter = 1
        errorMsg = '''        
        Your name has the following error(s):\n'''

        if rules[0]:
            errorMsg+= f'''         {counter}) It contains space(s) \n'''
            counter+=1
        if rules[1]:
            errorMsg+= f'''         {counter}) Your name is less than 7 characters \n'''
            counter+=1
        if rules[2]:
            errorMsg+= f'''         {counter}) Your name is more than 14 characters \n'''
            counter+=1
        if rules[3]:
            errorMsg+= f'''         {counter}) Your name has less than 2 numbers \n'''
            counter+=1
        if rules[4] and len(userInput) > 0:
            errorMsg+= f'''         {counter}) Your name contains special characters \n'''
            counter+=1
        print(errorMsg)
        return False