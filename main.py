'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game

Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''

import stages

player = stages.welcome()


for i in range(3):
    stages.triggerEventChoice(player, "morning")
    stages.triggerEventChoice(player, "afternoon")
    stages.triggerEventChoice(player, "night")
    player.day += 1

## end game

if player.stats["intelligence"] >= 150 and player.stats["strength"] >= 150 and player.stats["influence"] >=150:
    print("Congrats! You won her heart!")
else:
    print("Too bad, she doesn't love you back.")
print("Thanks for playing")



