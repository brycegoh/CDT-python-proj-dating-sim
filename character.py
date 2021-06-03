'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game
Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''

from random  import randint
class createCharacter:

    def __init__(self, name):
        self.name = name
    
    day = 1
    stats = {
        "intelligence": randint(75,130),
        "strength" : randint(75,130),
        "influence" : randint(75,130),

    }