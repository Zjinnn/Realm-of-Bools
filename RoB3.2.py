# Name: Bertan Berber
# Date: 21.04.2017
# Description: Text-based adventure game
# Version 3.2 Alpha

# -----------------------------------------------------------------------

import random
import time
import sys
import os

"""
class bcolors:
    BLACK = ''
    TEAL = ''
    PURPLE = ''
    BLUE = ''
    YELLOW = ''
    GREEN = ''
    RED = ''
    GRAY = ''
    ENDC = ''
    BOLD = ''
    UNDERLINE = ''

"""
class bcolors:
    BLACK = '\033[97m'
    TEAL = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    GRAY = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### Lister
### classList = ["1. Warrior", "2. Wizard", "3. Assassin"]
### locationList = ["1. Cave", "2. Castle", "3. Town"]
### itemList = ["1. Sword", "2. Staff", "3. Dagger"]

classList = ("""
    1. Warrior
    2. Wizard
    3. Rogue
    """)
locationList = ("""
    1. Cave
    2. Castle
    3. Town
    """)
#itemList = ("""
 #   1. Sword
  #  2. Staff
   # 3. Dagger
    #""")

northDirection = False
southDirection = False
westDirection = False
eastDirection = False
waitDirection = False

torch = False
rope = False
stone = False
char_wepinv = False
addInv = True


def charInventory():
    global addInv
    if addInv == "torch":
        printDelay(bcolors.YELLOW + "\n\nYou have acquired a torch!\n" + bcolors.ENDC)
    elif addInv == "rope":
        printDelay(bcolors.YELLOW + "\n\nYou have acquired a rope!\n" + bcolors.ENDC)
    elif addInv == "stone":
        printDelay(bcolors.YELLOW + "\n\nYou have acquired a stone!\n" + bcolors.ENDC)
    elif addInv == "char_wep":
        printDelay(bcolors.YELLOW + "\n\nYou have acquired a " + char_wep + "!\n" + bcolors.ENDC)


### Viser tekst en bokstav om ganngen:
def printDelay(text, delay=0.00): #(0.04)
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


### Viser feilmelding
def ErrorCode():
    print(bcolors.GRAY + "\nNot a valid input, please try again.\n" + bcolors.ENDC)


### Game Over
def playerDeath():
    global playAgain
    print(bcolors.RED + bcolors.BOLD + """\n
            You're dead.
             Game Over.\n""" + bcolors.ENDC)
    time.sleep(.6)
    playAgain = input("\nDo you wish to play again? (Y/N)\n"
                      "\n> ")
    if playAgain == "Y" or playAgain == "y":
        playAgain = "Y"
    elif playAgain == "N" or playAgain == "n":
        exit(0)
    else:
        print("Not a valid input, exiting game...")
        exit(0)


### Yay, du vant!
def playerWin():
    print(bcolors.GREEN + bcolors.BOLD + """\n
            You survived!
              You WIN!\n""" + bcolors.ENDC)
    time.sleep(.6)
    playAgain = input("\nDo you wish to play again? (Y/N)\n"
                      "> ")
    if playAgain == "Y" or playAgain == "y":
        playAgain = "Y"
    elif playAgain == "N" or playAgain == "n":
        exit(0)
    else:
        printDelay("Not a valid input, exiting game...")
        exit(0)


def locationKnowledge():
    printDelay("\nYou have already been to this place, there is nothing else to find.\n")
    printDelay("You go back to where you started.")


### Introduksjon
def displayIntro():
    printDelay(bcolors.BLUE + """
    Hello adventurer, welcome to the """ + bcolors.BOLD + bcolors.GREEN + """Realm of Bools!""" + bcolors.ENDC + bcolors.BLUE + """
    Your quest here is to survive an environment of your choosing.
    But there are many obstacles in your path,
    and you must find the safest path in order to proceed.\n
    """ + bcolors.ENDC)
    time.sleep(.6)


def chooseName():
    global char_name
    printDelay("To begin, type a name for your character.\n")
    char_name = input("\n> ")


### "for x in levelList:" Gjør det mulig for å vise lister vertikalt en etter en.
def chooseClass():
    print("\nChoose a class by typing the corresponding number.")
    print(classList)
    global char_class
    global char_wep
    char_class = True
    while char_class:
        char_class = input("> ")
        if char_class == "1":
            char_class = "Warrior"
            char_wep = "sword"
            break
        elif char_class == "2":
            char_class = "Wizard"
            char_wep = "magical staff"
            break
        elif char_class == "3":
            char_class = "Rogue"
            char_wep = "dagger"
            break
        else:
            ErrorCode()


##################################################################################################


def chooseLocation():
    print("\nChoose a starting location by typing the corresponding number.")
    print(locationList)
    global char_location
    char_location = True
    while char_location:
        char_location = input("> ")
        if char_location == "1":
            char_location = "Cave"
            break
        elif char_location == "2":
            char_location = "Castle"
            break
        elif char_location == "3":
            char_location = "Town"
            break
        else:
            ErrorCode()


##################################################################################################


def chooseDirection():
    print("\n\nWhat do you do?\n"
          "You can now type down a direction to choose a path. (Be creative)\n")
    global direction
    direction = True
    while direction:
        direction = input("> ")
        if direction == "right" or direction == "Right" or direction == "east" or direction == "East":
            direction = "E"
            break
        elif direction == "left" or direction == "Left" or direction == "west" or direction == "Wast":
            direction = "W"
            break
        elif direction == "forward" or direction == "Forward" or direction == "north" or direction == "North"\
                or direction == "front" or direction == "Front":
            direction = "N"
            break
        elif direction == "back" or direction == "Back" or direction == "south" or direction == "South":
            direction = "S"
            break
        elif direction == "wait" or direction == "Wait" or direction == "...":
            direction = "Wait"
            break
        else:
            ErrorCode()


##################################################################################################


def locationCave():
    global eastDirection
    global westDirection
    global northDirection
    global southDirection
    global waitDirection
    global torch
    global rope
    global addInv
    chooseDirection()
    if direction == "E":
        if torch == False:
            printDelay("\nAs you are walking to the right, you can smell something.\n"
                       "The smell is close to rotten flesh.\n")
            time.sleep(.6)
            printDelay("As you walk further into the darkness, you get a sense of emptiness.\n"
                       "You feel more and more drawn into the darkness as you walk,\n"
                       "it is as if you are not in control anymore.\n")
            time.sleep(.6)
            printDelay("...A light appears, it is getting closer.\n")
            time.sleep(.6)
            printDelay("Just as you reach the light, everything dissapears and that's it.")
            time.sleep(.6)
            playerDeath()
        elif torch == True and eastDirection == False:
            printDelay("\nAs you're walking to the right, you smell something.\n"
                       "You use the light from the torch to see that there\n"
                       "are dozens of dead rats on the floor.\n")
            time.sleep(.6)
            printDelay("You realize that there is poisonous gas and go back to\n"
                       "your starting area.\n")
            time.sleep(.6)
            printDelay("Thanks to your torch, you were able to avoid an unexpected death.\n"
                       "You return back to your starting point.")
            time.sleep(.6)
            eastDirection = True
            return locationCave()
        elif eastDirection == True:
            locationKnowledge()
            return locationCave()

    elif direction == "W":
        if torch == False and westDirection == False:
            printDelay("\nYou're walking to the left, as you're walking you can hear\n"
                       "a bell. It sounds like a bell from a church.\n")
            time.sleep(.6)
            printDelay("It gets louder the further you walk to it.\n"
                       "You're able to see a dark figure that looks like it is walking towards you.\n")
            time.sleep(.6)
            printDelay("You soon figure out that it was only your imagination and keep walking.\n"
                       "As you're walking something hits you in the head and the rest is unclear.\n")
            time.sleep(.6)
            printDelay("...You wake up after an hour in the same place. But now you have a lit torch.\n"
                       "You use the torch to go back to where you started.")
            time.sleep(.6)
            torch = True
            addInv = "torch"
            charInventory()
            westDirection = True
            return locationCave()
        elif torch == True or westDirection == True:
            locationKnowledge()
            return locationCave()

    elif direction == "N":
        if torch == False:
            printDelay("\nYou continue forward into the darkness...\n"
                       "After a few steps you fall into a pit and break 34 bones on impact.\n"
                       "You die a slow and painful death.")
            time.sleep(.6)
            playerDeath()

        elif torch == True and rope == False:
            printDelay("You continue forward into the darkenss...\n"
                       "Thanks to the light from your torch, you're able to go around a hole\n"
                       "on the ground and avoid death.\n")
            time.sleep(.6)
            printDelay("After a few more steps, you see light from the outside.\n"
                       "You get closer to the light source and see a hole 10 meters over the ground!\n"
                       "You can hear birds and the swift air from the outside and know this is\n"
                       "the way out!\n")
            time.sleep(.6)
            printDelay("But you need something to climb up there to get out.\n"
                       "Desperately you rush back to explore more to find something useful.")
            time.sleep(.6)
            northDirection = True
            return locationCave()

        elif torch == True and rope == False and northDirection == True:
            locationKnowledge()
            return locationCave()

        elif torch == True and rope == True and northDirection == False:
            printDelay("You continue forward into the darkenss...\n"
                       "Thanks to the light from your torch, you're able to go around a hole\n"
                       "on the ground and avoid death.\n")
            time.sleep(.6)
            printDelay("After a few more steps, you see light from the outside.\n"
                       "You get closer to the light source and see a hole 10 meters over the ground!\n"
                       "You can hear birds and the swift air from the outside and know this is\n"
                       "the way out!\n")
            time.sleep(.6)
            printDelay("You use your rope to climb out of the cave after many failed attempts.\n"
                       "But in the end you get out and smell the fresh air and think about how\n"
                       "lucky you were to be able to get out safe and sound.")
            time.sleep(.6)
            playerWin()

        elif torch == True and rope == True and northDirection == True:
            printDelay("Now with the rope, you desperately run back to the exit.\n"
                       "You use your rope to climb out of the cave after many failed attempts.\n"
                       "But in the end you get out and smell the fresh air and think about how\n"
                       "lucky you were to be able to get out safe and sound.")
            time.sleep(.6)
            playerWin()

    elif direction == "S":
        if torch == False and southDirection == False:
            printDelay("\nYou go back, further into the darkness...\n"
                       "While you're walking, you see what seems to be glowing eyes.\n"
                       "You don't think much of it and keep walking.\n")
            time.sleep(.6)
            printDelay("As you walk further the glowing eyes gets closer and you can soon hear growling\n"
                       "The moment you realize that there are predetors waiting for you it is too late.\n"
                       "Three animals jump on you and devour you alive.")
            time.sleep(.6)
            playerDeath()
        elif torch == True and northDirection == False and southDirection == False:
            printDelay("\nYou go back further into the darkness...\n"
                       "While you're walking you see three hungry wolves that doesn't dare to come\n"
                       "closer thanks to your torch.\n")
            time.sleep(.6)
            printDelay("At the end of the way, you find a rope. Hoping it will come in handy\n"
                       "you take it back with you.")
            time.sleep(.6)
            rope = True
            addInv = "rope"
            charInventory()
            southDirection = True
            return locationCave()
        elif torch == True and northDirection == True and southDirection == False:
            printDelay("\nYou go back further into the darkness...\n"
                       "While you're walking you see three hungry wolves that doesn't dare to come\n"
                       "closer thanks to your torch.\n")
            time.sleep(.6)
            printDelay("At the end of the way, you find a rope! Now that you have a rope\n"
                       "you rush back to the start in hopes that you didn't forget where the exit was.")
            time.sleep(.6)
            rope = True
            addInv = "rope"
            charInventory()
            southDirection = True
            return locationCave()
        elif southDirection == True:
            locationKnowledge()
            return locationCave()

    elif direction == "Wait":
        printDelay("You choose to wait there, hoping help will come to you rather than\n"
                   "risking your life trying to find a way out in complete darkness...\n")
        time.sleep(.6)
        printDelay("You die of thirst after 3 days and your body is forgotten forever\n"
                   "in a cave never to be seen again...")
        time.sleep(.6)
        playerDeath()


##################################################################################################


def locationCastle():
    chooseDirection()


##################################################################################################


def locationTown():
    chooseDirection()


##################################################################################################


playAgain = "Y"
while playAgain == "Y" or playAgain == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    displayIntro()
    ### Gir brukeren sjansen til å starte på nytt.
    reselect = "N"
    while reselect == "N" or reselect == "n":
        chooseName()
        chooseClass()
        chooseLocation()
        reselect = input("\nYour name is " + char_name.capitalize() + " and you are a "
                         + char_class + " located in a " + char_location + ".\n"
                         "Do you want to continue?\n"
                         "Press 'Enter' to continue your journey with your current character.\n"
                         "Type N to start over.\n"
                         "\n> ")
        if reselect == "Y" or reselect == "y":
            reselect = "Y"
        elif reselect == "N" or reselect == "n":
            reselect = "n"
    ### ^^Gir brukeren sjansen til å velge på nytt.^^

    if char_location == "Cave":
        os.system('cls' if os.name == 'nt' else 'clear')
        printDelay("\n...You wake up in a wet, dark place. You can barely see your own hands.\n")
        time.sleep(.6)
        printDelay("You have no idea how you ended up in this eerie place\n"
                   "and you have to find a way out.\n")
        time.sleep(.6)
        printDelay("But be careful, the enviroment is dangerous,\n"
                   "you might fall down a hole and get trapped...")
        time.sleep(.6)
        locationCave()

    elif char_location == "Castle":
        os.system('cls' if os.name == 'nt' else 'clear')
        printDelay("\nIt appears you were captured by some knights and taken to this castle.\n")
        time.sleep(.6)
        printDelay("There is a gate ahead, but it's locked.\n"
                   "In order to get out you need to find the key.\n")
        time.sleep(.6)
        printDelay("But watch out for the knights, they are still walking around the castle...")
        time.sleep(.6)
        locationCastle()

    elif char_location == "Town":
        os.system('cls' if os.name == 'nt' else 'clear')
        printDelay("\nYour town is in danger, there are bandits raiding your town while\n"
                   "slaughtering and raping your friends.\n")
        time.sleep(.6)
        printDelay("You need to save your people, and to do that you need a weapon.\n")
        time.sleep(.6)
        printDelay("But be careful, don't let the bandits see you while you're\n"
                   "searching for a weapon, or else they might do very unpleasant things to you...")
        time.sleep(.6)
        locationTown()