# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:17:13 2015

@author: Erik
"""

import numpy as np
import math as ma
import matplotlib.pyplot as plt

def LindIter(system, n, rule1, rule2):
    """Returns a string containing a sequence of symbols, which define a Lindenmayer system.
    The input system defines the Lindemayer system and n its iterations"""
#Produces a Lidenmayerstring based on the Koch system.
#Use 7 iterations at most.
    if system=="koch":
        Lidenmayerstring="S"
        for i in range(n):
            Lidenmayerstring=Lidenmayerstring.replace("S","SLSRSLS")
#Produces a Lidenmayerstring based on the Sierpinski system.
#Use 9 iterations at most.
    elif system=="sierpinski":
        Lidenmayerstring="A"
        for i in range(n):
            Lidenmayerstring=Lidenmayerstring.replace("A","E")
            Lidenmayerstring=Lidenmayerstring.replace("B","ALBLA")
            Lidenmayerstring=Lidenmayerstring.replace("E","BRARB")
#User defined system 1.
    elif system=="user defined 1":
        Lidenmayerstring="S"
        for i in range(n):
            Lidenmayerstring=Lidenmayerstring.replace("S",rule1)
#User defined system 2.
    elif system=="user defined 2":
        Lidenmayerstring="A"
        for i in range(n):
            Lidenmayerstring=Lidenmayerstring.replace("A","E")
            Lidenmayerstring=Lidenmayerstring.replace("B",rule2)
            Lidenmayerstring=Lidenmayerstring.replace("E",rule1)
    return Lidenmayerstring


def turtleGraph(LindenmayerString,leftangle,rightangle,iterations):
    """
    Translates a lindenmayerstring(input) into graphic commands in the form of 
    lengths and turns. Output is an array containing numbers alternating between
    lengths (scalar) and turns (radians)
    """
#Finding out the type of Lindenmayerstring
#If single rule system:
    turtleCommands=np.array([])
    if "S" in LindenmayerString:
        if iterations==0:
            Forward=1
        else:
            Forward=1.0/(3**iterations)
#Translates letters into numbers, S is a length, R and L is turn angles
        for i in range(len(LindenmayerString)):
            if LindenmayerString[i]=="S":
                turtleCommands=np.append(turtleCommands,Forward)
            elif LindenmayerString[i]=="R":
                Right=-(ma.pi/180)*rightangle
                turtleCommands=np.append(turtleCommands,Right)
            elif LindenmayerString[i]=="L":
                Left=(ma.pi/180)*leftangle
                turtleCommands=np.append(turtleCommands,Left)
#If two rule system:
    elif "A" in LindenmayerString:
        if iterations==0:
            Forward=1
        else:
            Forward=1.0/(2**iterations)
#Translates letters into numbers, S is a length, R and L is turn angles
        for i in range(len(LindenmayerString)):
            if LindenmayerString[i]=="A" or LindenmayerString[i]=="B":
                turtleCommands=np.append(turtleCommands,Forward)
            elif LindenmayerString[i]=="R":
                Right=-(ma.pi/180)*rightangle
                turtleCommands=np.append(turtleCommands,Right)
            elif LindenmayerString[i]=="L":
                Left=(ma.pi/180)*leftangle
                turtleCommands=np.append(turtleCommands,Left)
    return turtleCommands


def turtlePlot(turtleCommands,color,system,iterations):
    """ 
    Takes an array of alternating lenghts and turns to plot a diagram
    according to user defined colors, turtleCommands is an array of numbers,
    color is a string, system is a string, iterations is an integer 
    """
#Start-point and start-direction
    X0=np.array([0])
    Y0=np.array([0])
    d0=np.array([1,0])
#Translation of array into two arrays containing x and y values using that
#element values alternate between length and turn angle
    for i in range(np.size(turtleCommands)):
        if i//2==i/2:
            Li=turtleCommands[i]
            if i==0:
                Xi=X0+d0[0]*Li
                Yi=Y0+d0[1]*Li
                X0=np.append(X0,Xi)
                Y0=np.append(Y0,Yi)
                di1=d0
            else:
                di1=np.dot(np.array([[ma.cos(Ti),-ma.sin(Ti)],[ma.sin(Ti),ma.cos(Ti)]]),di1)
                Xi=Xi+Li*di1[0]
                X0=np.append(X0,Xi)
                Yi=Yi+Li*di1[1]
                Y0=np.append(Y0,Yi)
        else:
            Ti=turtleCommands[i]
#Plot of figure and making name change according to type of plot and iteration
    plt.figure(1)
    plt.plot(X0,Y0,color)
    LinderName=system+" - "+str(iterations)
    plt.xlim([min(X0),max(X0)])
    plt.title(LinderName)
    plt.show()


#Main script:
mainmenu=" Main menu: \n 1. Set specifications \n 2. Define custom system \n 3. Graph color \n 4. Generate plot \n 5. Quit \n"
lindenmayermenu=" Set specifications: \n 1. Set system \n 2. Set iterations \n 3. Set angles \n 4. Go back \n"
systemmenu=" Set system: \n (this will reset iterations and angle values) \n 1. Koch curve \n 2. Sierpinski triangle \n 3. User defined \n 4. Go back \n"
colormenu=" Graph colors: \n 1. Blue \n 2. Green \n 3. Red \n 4. Black \n 5. Magenta \n 6. Go back \n"
anglemenu=" Angles: \n 1. Left angle \n 2. Right angle \n 3. Go back \n"
usermenu1=" Number of rules: \n 1. One rule \n 2. Two rules \n"
usermenu2=" Next action: \n 1. Left \n 2. Right \n"
usermenu3=" Next action: \n 1. Rule 1 (A) \n 2. Rule 2 (B) \n"
usermenu4=" Next action: \n 1. Continue \n 2. Stop \n"
usermenu5=" Are you sure that you would like to delete the current user defined system? \n 1. Yes \n 2. No \n"

system="none"
iterations="none"
leftangle="none"
rightangle="none"
color="k-"
rule1="none"
rule2="none"

def variables():
    return " | System: "+system+" | Iterations: "+str(iterations)+" | \n | Left: "+str(leftangle)+" | Right: "+str(rightangle)+" | \n"

def rules():
    return " | Rule 1: "+rule1+" | Rule 2: "+rule2+" |"

#Main menu:
print(mainmenu+variables())
while True:
    action1=input("Please choose an action: ")
#Set specifications:
    if action1.lower()=="set specifications" or action1=="1":
        print(lindenmayermenu+variables())
        while True:
            action2=input("Please choose an action: ")
#System menu:
            if action2.lower()=="set system" or action2=="1":
                print(systemmenu+variables()+rules())
                while True:
                    action3=input("Please choose an action: ")
                    if action3.lower()=="koch curve" or action3=="1":
                        system="koch"
                        iterations="none"
                        leftangle=60
                        rightangle=120
                        print(lindenmayermenu+variables())
                        break
                    elif action3.lower()=="sierpinski triangle" or action3=="2":
                        system="sierpinski"
                        iterations="none"
                        leftangle=60
                        rightangle=60
                        print(lindenmayermenu+variables())
                        break
                    elif action3.lower()=="user defined" or action3=="3":
                        if rule1!="none" and rule2=="none":
                            system="user defined 1"
                            iterations="none"
                            leftangle="none"
                            rightangle="none"
                            print(lindenmayermenu+variables())
                            break
                        elif rule1!="none" and rule2!="none":
                            system="user defined 2"
                            iterations="none"
                            leftangle="none"
                            rightangle="none"
                            print(lindenmayermenu+variables())
                            break
                        elif rule1=="none" and rule2=="none":
                            print(lindenmayermenu+variables())
                            print("Please define a user defined system before setting it.")
                            break
                    elif action3.lower()=="go back" or action3=="4":
                        print(lindenmayermenu+variables())
                        break
                    else:
                        print(systemmenu+variables())
                        print("Action doesn't exist.")
#Iterations menu:
            elif action2.lower()=="set iterations" or action2=="2":
                if system=="koch":
                    while True:
                        action4=input("Please enter an integer between 0 and 7: ")
                        try:
                            if int(action4)<0 or int(action4)>7:
                                print("Not a valid value")
                            else:
                                iterations=int(action4)
                                print(lindenmayermenu+variables())
                                break
                        except ValueError:
                            print("Not a valid value")
                elif system=="sierpinski":
                    while True:
                        action4=input("Please enter an integer between 0 and 9: ")
                        try:
                            if int(action4)<0 or int(action4)>9:
                                print("Not a valid value")
                            else:
                                iterations=int(action4)
                                print(lindenmayermenu+variables())
                                break
                        except ValueError:
                            print("Not a valid value")
                elif system=="user defined 1" or system=="user defined 2":
                    while True:
                        print("This is a user defined system. Therefore start with few iterations and gradually move up to avoid the program stalling!")
                        action4=input("Please enter an non negative integer: ")
                        try:
                            if int(action4)<0:
                                print("Not a valid value")
                            else:
                                iterations=int(action4)
                                print(lindenmayermenu+variables())
                                break
                        except ValueError:
                            print("Not a valid value")
                elif system=="none":
                    print(lindenmayermenu+variables())
                    print("Please set a system before setting iterations")
#Angle menu:
            elif action2.lower()=="set angles" or action2=="3":
                print(anglemenu+variables())
                while True:
                    if system=="none":
                        print(lindenmayermenu+variables())
                        print("Please set a system before setting angles")
                        break
                    action6=input("Please choose an action: ")
                    if action6.lower()=="left angle" or action6=="1":
                        while True:
                            try:
                                leftangle=float(input("Please choose a left angle: "))
                                print(anglemenu+variables())
                                print("Left angle has been set")
                                break
                            except ValueError:
                                print("Not a valid value")
                    elif action6.lower()=="right angle" or action6=="2":
                        while True:
                            try:
                                rightangle=float(input("Please choose a right angle: "))
                                print(anglemenu+variables())
                                print("Right angle has been set")
                                break
                            except ValueError:
                                print("Not a valid value")
                    elif action6.lower()=="go back" or action6=="3":
                        print(lindenmayermenu+variables())
                        break
                    else:
                        print(anglemenu+variables())
                        print("Action doesn't exist.")
            elif action2.lower()=="go back" or action2=="4":
                print(mainmenu+variables())
                break
            else:
                print(lindenmayermenu+variables())
                print("Action doesn't exist.")
#Define custom system:                
    elif action1.lower()=="define custom system" or action1=="2":
        break0=False
        if rule1!="none":
            print(usermenu5+rules())
            while True:
                action16=input("Please choose an action: ")
                if action16.lower()=="yes" or action16=="1":
                    break
                elif action16.lower()=="no" or action16=="2":
                    break0=True
                    break
                else:
                    print(usermenu5+rules())
                    print("Action doesn't exist.")
        if break0==True:
            print(mainmenu+variables())
            continue
        
        system="none"
        iterations="none"
        leftangle="none"
        rightangle="none"
        rule1="none"
        rule2="none"
        break1=False
        break2=False
        print(usermenu1+rules())
        while True:
            action7=input("Please choose an action: ")
#One rule:
#Define rule 1
            if action7.lower()=="one rule" or action7=="1":
                rule1="S"                
                while True:
                    if rule1[-1]=="S":
                        print(usermenu2+rules())
                        while True:
                            action8=input("Please choose an action: ")
                            if action8.lower()=="left" or action8=="1":
                                rule1=rule1+"L"
                                break
                            elif action8.lower()=="right" or action8=="2":
                                rule1=rule1+"R"
                                break
                            else:
                                print(usermenu2+rules())
                                print("Action doesn't exist.")
                    if rule1[-1]!="S":
                        rule1=rule1+"S"
                        print(usermenu4+rules())
                        while True:
                            action9=input("Please choose an action: ")
                            if action9.lower()=="continue" or action9=="1":
                                break
                            elif action9.lower()=="stop" or action9=="2":
                                break1=True
                                break
                            else:
                                print(usermenu4+rules())
                                print("Action doesn't exist.")
                    if break1==True:
                        break
                if break1==True:
                    print(mainmenu+variables())
                    print("User defined system has been set")
                    break
#Two rules:
#Define rule 1
            elif action7.lower()=="two rules" or action7=="2":
                if rule1=="none":
                    print(usermenu3+rules())
                    while True:
                        action20=input("Please choose an action: ")
                        if action20.lower()=="rule 1 (a)" or action20=="1":
                            rule1="A"
                            break
                        elif action20.lower()=="rule 2 (b)" or action20=="2":
                            rule1="B"
                            break
                        else:
                            print(usermenu3+rules())
                            print("Action doesn't exist.")
                while True:
                    if rule1[-1]=="A" or rule1[-1]=="B":
                        print(usermenu2+rules())
                        while True:
                            action10=input("Please choose an action: ")
                            if action10.lower()=="left" or action10=="1":
                                rule1=rule1+"L"
                                break
                            elif action10.lower()=="right" or action10=="2":
                                rule1=rule1+"R"
                                break
                            else:
                                print(usermenu2+rules())
                                print("Action doesn't exist.")
                    if rule1[-1]!="A" or rule1[-1]!="B":
                        print(usermenu3+rules())
                        while True:
                            action11=input("Please choose an action: ")
                            if action11.lower()=="rule 1 (a)" or action11=="1":
                                rule1=rule1+"A"
                                print(usermenu4+rules())
                                break
                            elif action11.lower()=="rule 2 (b)" or action11=="2":
                                rule1=rule1+"B"
                                print(usermenu4+rules())
                                break
                            else:
                                print(usermenu3+rules())
                                print("Action doesn't exist.")
                        while True:
                            action12=input("Please choose an action: ")
                            if action12.lower()=="continue" or action12=="1":
                                print(usermenu2+rules())
                                break
                            elif action12.lower()=="stop" or action12=="2":
                                if rule1[0]=="A":
                                    if not "B" in rule1:
                                        print(usermenu4+rules())
                                        print("Rule 1 needs to contain the letter B")
                                        continue
                                    else:
                                        break1=True
                                        break
                                elif rule1[0]=="B":
                                    if not "A" in rule1:
                                        print(usermenu4+rules())
                                        print("Rule 1 needs to contain the letter A")
                                        continue
                                    else:
                                        break1=True
                                        break
                            else:
                                print(usermenu4+rules())
                                print("Action doesn't exist.")
                    if break1==True:
                        break
#Define rule 2
                if rule2=="none":
                    print(usermenu3+rules())
                    print(" Rule 1 have been defined. \n You are now defining rule 2.")
                    while True:
                        action21=input("Please choose an action: ")
                        if action21.lower()=="rule 1 (a)" or action21=="1":
                            rule2="A"
                            break
                        elif action21.lower()=="rule 2 (b)" or action21=="2":
                            rule2="B"
                            break
                        else:
                            print(usermenu3+rules())
                            print("Action doesn't exist.")
                while True:
                    if rule1[-1]=="A" or rule1[-1]=="B":
                        print(usermenu2+rules())
                        while True:
                            action13=input("Please choose an action: ")
                            if action13.lower()=="left" or action13=="1":
                                rule2=rule2+"L"
                                break
                            elif action13.lower()=="right" or action13=="2":
                                rule2=rule2+"R"
                                break
                            else:
                                print(usermenu2+rules())
                                print("Action doesn't exist.")
                    if rule1[-1]!="A" or rule1[-1]!="B":
                        print(usermenu3+rules())
                        while True:
                            action14=input("Please choose an action: ")
                            if action14.lower()=="rule 1 (a)" or action14=="1":
                                rule2=rule2+"A"
                                print(usermenu4+rules())
                                break
                            elif action14.lower()=="rule 2 (b)" or action14=="2":
                                rule2=rule2+"B"
                                print(usermenu4+rules())
                                break
                            else:
                                print(usermenu3+rules())
                                print("Action doesn't exist.")
                        while True:
                            action15=input("Please choose an action: ")
                            if action15.lower()=="continue" or action15=="1":
                                print(usermenu2+rules())
                                break
                            elif action15.lower()=="stop" or action15=="2":
                                break2=True
                                break
                            else:
                                print(usermenu4+rules())
                                print("Action doesn't exist.")
                    if break2==True:
                        break
                if break2==True:
                        print(mainmenu+variables())
                        print(" User defined system has been set")
                        break
            else:
                print(usermenu1+rules())
                print("Action doesn't exist.")
#Color menu:
    elif action1.lower()=="graph color" or action1=="3":
        print(colormenu+variables())
        while True:
            action5=input("Please choose an action: ")
            if action5.lower()=="blue" or action5=="1":
                color="b-"
                print(mainmenu+variables())
                print("Color has been set")
                break
            elif action5.lower()=="green" or action5=="2":
                color="g-"
                print(mainmenu+variables())
                print("Color has been set")
                break
            elif action5.lower()=="red" or action5=="3":
                color="r-"
                print(mainmenu+variables())
                print("Color has been set")
                break
            elif action5.lower()=="black" or action5=="4":
                color="k-"
                print(mainmenu+variables())
                print("Color has been set")
                break
            elif action5.lower()=="magenta" or action5=="5":
                color="m-"
                print(mainmenu+variables())
                print("Color has been set")
                break
            elif action5.lower()=="go back" or action5=="6":
                print(mainmenu+variables())
                break
            else:
                print(colormenu+variables())
                print("Action doesn't exist.")
#Generate plots:
    elif action1.lower()=="generate plot" or action1=="4":
        if system=="none":
            print(mainmenu+variables())
            print("Please set system before generating plot")
        elif iterations=="none":
            print(mainmenu+variables())
            print("Please set iterations before generating plot")
        elif leftangle=="none" or rightangle=="none":
            print(mainmenu+variables())
            print("Please set all angles before generating plot")
        else:
            print(mainmenu+variables())
            turtlePlot(turtleGraph(LindIter(system, iterations, rule1, rule2),leftangle,rightangle,iterations),color,system,iterations)
#Quit and error:
    elif action1.lower()=="quit" or action1=="5":
        print("Program closed.")
        break
    else:
        print(mainmenu+variables())
        print(" Action doesn't exist.")