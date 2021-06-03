'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game

Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''
# dependancies
import random
import time
import util
# tic tac toe functions
from tictactoeFunctions import tictactoeStart
## misc data for minigame imports
import historyQuizQuestionBank
from hangmanPrints import hangmanPrints


def distributeRewards(player, awards, pointsToMinusOff = 0):
    for (key, value) in awards.items():
        player.stats[key] += (value - pointsToMinusOff)
    return

def startHistoryQuiz( player , event ):
    award = event["awards"]
    event["completionStatus"] = True
    questions = historyQuizQuestionBank.questions
    marks = 0
    print("To pass this Quiz, you have to get at least 3 questions correct. The topic is Singapore History.")
    for number in questions:
        print( number['query'] )
        playerAnswer = input("Please choose (a,b,c)").strip()
        while playerAnswer not in ['a','b','c']:
            print("Please only input a or b or c")
            playerAnswer = input("Please choose (a,b,c)").strip()
        if playerAnswer == number['answer']:
            marks += 1
        else:
            continue
    if marks > 3:
        print(f"You got {marks} marks, congratulations on passing!")
        distributeRewards( player , award[0])
    else:
        print(f"You got {marks} marks, you did not make it.")
    
    return

def tictactoeGame( player , event ):
    award = event["awards"]
    board = []
    for i in range(9):
        board.append(" ")
    winOrLose = tictactoeStart(board)
    if winOrLose:
        distributeRewards( player , award[0])
    event["completionStatus"] = True
    return

def mathClassMiniGame(player , event):
    awards = event["awards"]
    operators = [ "+" , "-" , "*" , "//" ]
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    op = random.choice(operators)
    expression = f" {number1} {op} {number2} "
    answer = eval(expression)
    playerAnswer = util.floatInput( f"\nEvaluate the following: {expression} = " )
    event["completionStatus"] = True
    if playerAnswer == answer :
        distributeRewards(player, awards[0])
        print("Correct! Well done!\n")
        return True
    else:
        print(f"You got it wrong... Answer is {answer}\n")
        return False

def hangmanMiniGame(player, event):
    print("Welcome to the hangman minigame")
    event["completionStatus"] = True
    awards = event["awards"]
    wordFileList = open("./textFiles/words.txt", 'r').read().splitlines()
    randomWord = random.choice(wordFileList[4:])
    container =['_']*len(randomWord)
    alphaGuessedBefore = []
    errors = 0
    print(f'''{hangmanPrints[errors]}''')
    print(" ".join(container)  )
    while errors < 6:
        while True:  
            guessedAlpha = input("Guess an alphabet: ").lower()
            warning = "Your input has the following error(s): \n"
            rules = [
                len(guessedAlpha) == 1,
                guessedAlpha.isalpha(),
                guessedAlpha not in alphaGuessedBefore
            ]
            if all( rules ):
                break
            else:
                counter = 1
                if not rules[0]:
                    warning += f"{counter}) Please enter only 1 alphabet.\n"
                    counter+=1
                if not rules[1]:
                    warning += f"{counter}) You entered a special character. Please enter a alphabet.\n"
                    counter+=1
                if not rules[2]:
                    warning += f"{counter}) You guessed this alphabet before! Please try another alphabet.\n"
                    counter+=1
                print(warning)

        if guessedAlpha in randomWord:
            alphaGuessedBefore.append(guessedAlpha)
            indexs = [ i for (i,v) in enumerate(randomWord) if v == guessedAlpha ]
            for i in indexs:
                container[i] = guessedAlpha
            if "".join(container) == randomWord:
                print("success")
                distributeRewards(player, awards[0])
                return
        else:
            alphaGuessedBefore.append(guessedAlpha)
            errors += 1
        print(f'''{hangmanPrints[errors]}''')
        print(" ".join(container)  )
    print("GGWP")
    return 


def typingTestMiniGame(player , event):
    awards = event["awards"]
    wordFileList = open("./textFiles/words.txt", 'r').read().splitlines()
    listOfWords = random.sample(wordFileList[4:], 5)
    print("\nYes... typing is a sport...\n")
    while True:
        start = input("Enter 'start' to start the typing game: ").strip()
        if start == "start":
            print("Game will begin in: ")
            break
        else:
            print("Invalid input!")

    for i in [3,2,1]:
        print(i)
        time.sleep(1)
    print("START TYPING \n")

    errors = 0
    correctAlphaTyped = 0

    startTime = time.time() #seconds in epoch time
    for word in listOfWords:
        inputWords = input(f"Type '{word}' :").strip()
        for ( userAlpha , actualAlpha ) in zip( inputWords , word ): # will only loop over length of shortest string
            if userAlpha == actualAlpha:
                correctAlphaTyped += 1
        if inputWords != word:
            errors += 1
    endTime = time.time()
    totalTime = endTime - startTime #seconds
    event["completionStatus"] = True
    print(f"\nNumber of word(s) typed wrongly: {errors}")
    print(f"Alphabets typed correctly per second : {round(correctAlphaTyped / totalTime , 2)}")
    distributeRewards(player, awards[0], errors)
    return 

def askForOptions(player , event, lengthOfOptions):
    userChoice = util.integerInput("Please choose one: ")
    while userChoice < 1 or userChoice > lengthOfOptions:
        print("invalid choice")
        userChoice = util.integerInput("Please choose one: ")
    requirementForOption = event["optionsRequirement"][userChoice - 1]
    rule = []
    statsLacking = "You are lacking in the following stats:\n"
    for (key, value) in requirementForOption.items():
        isDoable = player.stats[key] >= value
        rule.append( isDoable )
        if not isDoable:
            statsLacking+= f"{requirementForOption[key] - player.stats[key]} {key}\n"
    isOptionDoable = all(rule)
    if not isOptionDoable:
        print("Option is not viable for your current stats")
        print(statsLacking)
        return askForOptions(player, event, lengthOfOptions)
    else:
        return userChoice

def triggerDialogue (player,event):
    with open (event["dialogueFile"],'r') as f:
        listOfLines = f.read().splitlines()
        optionsIndex = listOfLines.index("--options--")
        endIndex = listOfLines.index("--end--")
        
        diagList = listOfLines[:optionsIndex]
        optionsList = listOfLines[optionsIndex+1:endIndex]
        diagAfterOptions = listOfLines[endIndex+1:]

        for diag in diagList:
            if "--NAME--" in diag:
                diag = diag.replace("--NAME--", player.name) ##bryce
            print(diag)
            time.sleep(1)
        print("\n----Choose an option----")
        for options in optionsList:
            print(options)
        
        optionChoosen = askForOptions(player, event, len(optionsList))
            
        for line in diagAfterOptions:
            print(line)
        
        distributeRewards(player, event["awards"][optionChoosen - 1])
        event["completionStatus"] = True
        return


        


