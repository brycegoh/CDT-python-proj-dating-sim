'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game

Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''

from character import createCharacter
from events import events
import random
import util

def welcome():
    name = input('''
You have 3 days to make her fall in love with you, 
and on each day you have 3 chances to either increase your 
1. intelligence, 
2. physical strength, 
or deepen your relationship with the girl. 

You play minigames to increase your intelligence and strength stat, 
while having dialogues with the girl can increase her attraction towards you, 
but choose when you want to talk to her as only certain response options will be unlocked only after you attain a certain stat level. 

By the end of the 3 days, 
you will need to hit a certain level of intelligence, physical strength and influence in order to win her heart and thus win the game.


Welcome to the game.
Please choose a name, ensuring that your name is the following:
    1. Between 7 to 14 characters.
    2. Contains at least 2 numbers.
    3. Contains no spaces.
    4. Contains no special characters.

Enter your character name: ''')
    while not util.validateString( name ):
        name = input("        Please choose another name: ")
    player = createCharacter(name)
    return player

def getAllPossibleEvents( timeframe ):
    possibleEvents = [x for x in events if not x["completionStatus"] and x["timeframe"] == timeframe]
    return possibleEvents
 
def showCurrentStats( player ):
    container = "Your stats are :\n"
    stats = player.stats
    for (key,value) in stats.items():
        container += f"{key} : {value}\n"
    print(container)
    return 

def optionInputLoop(maxNumber, player):
    choice = util.integerInput("Choose an event to do today : ")
    if choice == maxNumber+1:
        showCurrentStats(player)
        return optionInputLoop(maxNumber, player)
    elif (choice > maxNumber+1 or choice < 1):
        print("Invalid choice")
        return optionInputLoop(maxNumber, player)
    else:
        return choice

def askUserToChooseOption( events, player ):
    choice = None
    counter = 1
    for eachEvent in events:
        print(f'{counter}) {eachEvent["title"]}\n')
        counter+=1
    print(f'{counter}) Show stats\n')
    choice = optionInputLoop( len(events), player )
    return events[choice-1] 

def triggerEventChoice(player, timeframe):
    print( f"Day {player.day} : {timeframe} options as follows" )
    randomEvent = askUserToChooseOption(getAllPossibleEvents(timeframe), player)
    randomEvent["start"]( player, randomEvent )
    return

    
   