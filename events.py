'''
Cohort Class 10 Group 08 - CTD 1D Project - Dating simulator text based game

Goh Ying Ming, Bryce	                1005016

Melodie Chew En Qi	                    1005319

Atisha Teriyapirom	                    1005244

Mohamad Arman Bin Mohamad Nasser	    1005135
'''


'''
Template of the dictionary is as such

{
    "title": STRING,      | describes the event                          

    "start": FUNCTION REFERENCE FROM eventFunctions ,        | reference to the function to start the event

    "awards": [
        { 
            STRING : INT       | List of dictionaries which corresponds to the number of options
        }
    ],

    "completionStatus": BOOLEAN,     | Event complete: True or False -> DEFAULT IS FALSE

    "timeframe": STRING,        | morning , afternoon , night

    "dialogueFile": STRING,        | filepath to the .txt file -> "./textFiles/yourFileName.txt"

    "optionsRequirement": [
        {
            STRING: INT             | requirement for each option
        }
    ] 
}
'''

import eventFunctions

events = [
    {
        "title": "PE Class: Finger movements",                          

        "start": eventFunctions.typingTestMiniGame ,

        "awards": [{ 
            "strength": 40       
        }],

        "completionStatus": False,       

        "timeframe": "morning",  

            "dialogueFile": '',

        "optionsRequirement": [] 
    },
    
    {
        "title": "Attend Math Class",                          

        "start": eventFunctions.mathClassMiniGame ,

        "awards": [{ 
            "intelligence": 50       
        }],

        "completionStatus": False,       

        "timeframe": "morning",  

            "dialogueFile": '',

        "optionsRequirement": [] 
    },
    {
        "title": "Do you think I'm...",                          

        "start": eventFunctions.triggerDialogue ,

        "awards": [
            { 
                "intelligence": 40 ,
                "influence":30       
            },
            {
                "influence":60
            },
            {
                "influence":-10
            }
        ],

        "completionStatus": False,       

        "timeframe": "morning",  

            "dialogueFile": './textFiles/doyouthink.txt',

        "optionsRequirement": [
            {
                "intelligence": 100 , 
            },
            {
                "intelligence": 50 , 
                "strength": 100 
            }, 
            {

            }
        ] 
    },
    {
        "title": "Attend Science Class",                          

        "start": eventFunctions.tictactoeGame ,

        "awards": [{ 
            "intelligence": 40       
        }],

        "completionStatus": False,       

        "timeframe": "afternoon",  

            "dialogueFile": '',

        "optionsRequirement": [] 
    },
    {
        "title": "Take English Class",                          

        "start": eventFunctions.hangmanMiniGame ,

        "awards": [{ 
            "strength": 40       
        }],

        "completionStatus": False,       

        "timeframe": "afternoon",  

            "dialogueFile": '',

        "optionsRequirement": [] 
    },
    {
        "title": "After school studying",                          

        "start": eventFunctions.triggerDialogue ,

        "awards": [
            { 
                "influence": 50,
                "intelligence":60     
            },
            {
                "influence":40,
                "strength":35
            },
            {
                "intelligence":30
            }
        ],

        "completionStatus": False,       

        "timeframe": "afternoon",  

            "dialogueFile": './textFiles/afterschoolstudying.txt',

        "optionsRequirement": [
            {
            "intelligence": 110 , 
            },
            {
            "strength": 105 
            },
            {

            }
        ]  
    },
    {
        "title": "Attend History Class",                          

        "start": eventFunctions.startHistoryQuiz ,

        "awards": [{ 
            "intelligence": 50     
        }],

        "completionStatus": False,       

        "timeframe": "night",  

            "dialogueFile": '',

        "optionsRequirement": [] 
    },
    {
        "title": "Gym Session",                          

        "start": eventFunctions.typingTestMiniGame ,

        "awards": [{ 
            "strength": 30       
        }],

        "completionStatus": False,       

        "timeframe": "night",  

            "dialogueFile": '',

        "optionsRequirement": []  
    },
    {
        "title": "In the rain",                          

        "start": eventFunctions.triggerDialogue ,

        "awards": [
            { 
                "influence": 50     
            },
            {
                "influence":30
            },
            {
                "strength": -10
            }
        ],

        "completionStatus": False,       

        "timeframe": "night",  

            "dialogueFile": './textFiles/intherain.txt',

        "optionsRequirement": [
            {
                "intelligence": 150 , 
            },
            {
                "strength": 120 
            },
            {

            }
        ]  
    }
]