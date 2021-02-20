'''
Created on Feb 19, 2021

@author: ITAUser
'''
def fixMyCar(problem):
    if(problem == "tire"):
        print("Replace tires.")
    elif(problem == "headlight"):
        print("Fill headlight fluid.")
    elif(problem == "door"):
        print("replace door")
    elif(problem == "gas"):
        print("Fill gas tank")
    elif(problem == "window"):
        print("Replace window")
    elif(problem == "wipers"):
        print("Replace wipers")
    elif(problem == "battery"):
        print("Replace battery")
    elif(problem == "exhaust"):
        print("Replace exhaust system")
    if(problem == "transmission"):
        print("Throw out car")
    if("nothing"):
        print("Your car is fine.")
    
    return 

fixMyCar("tire")
fixMyCar("headlight")
fixMyCar("door")
fixMyCar("gas")
fixMyCar("window")
fixMyCar("wipers")
fixMyCar("battery")
fixMyCar("exhaust")
fixMyCar("transmission")
fixMyCar("Nothing")