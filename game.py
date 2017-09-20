import time
import datetime
import os

print("\033[2J\033[0;0H")
print("\t****************************")
print("\t****************************")
print("\t*****  \033[1;34mPokémon\033[0m \033[1;32mPYTHON\033[0m  *****")
print("\t****************************")
print("\t****************************")
time.sleep(1)
print("""\

             _.--""`-..
            ,'          `.
          ,'          _   `.
                     " __   
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       
      ._     '           _'  |                    
      `.`-...___,...---""    |       
       - .`._        _,-,.'   .                

Made in \033[1;32mPython\033[0m to feed your nostalgia!                   
                    """)

time.sleep(1)

def startGame():
    input('Press enter to begin...')
startGame()

myName = input('\nWhat\'s your name? ')
pikachu = '\033[1;33mPikachu\033[0m'
bulbasaur = '\033[1;32mBulbasaur\033[0m' 
charmander = '\033[1;31mCharmander\033[0m' 
squirtle = '\033[1;36mSquirtle\033[0m'
newL = '\n'
# late = False
myPokemon = 'CHANGE'
garyPokemon = 'CHANGE'
choicePrompt = '\033[3mchoose a number to act\033[0m'
choice1 = '\033[1;35m 1.\033[0m'
choice2 = '\033[1;35m 2.\033[0m'
choice3 = '\033[1;35m 3.\033[0m'
choice4 = '\033[1;35m 4.\033[0m'

print('\nThanks. Enjoy the game!')
time.sleep(2)
print("\033[2J\033[0;0H")

dayOfWeek = datetime.datetime.today().weekday()
if dayOfWeek == 0:
    day = 'Monday'
elif dayOfWeek == 1:
    day = 'Tuesday'
elif dayOfWeek == 2:
    day = 'Wednesday'
elif dayOfWeek == 3:
    day = 'Thursday'
elif dayOfWeek == 4:
    day = 'Friday'
elif dayOfWeek == 5:
    day = 'Saturday'
elif dayOfWeek == 6:

    day = 'Sunday'


#

def garyBattle(myPokemon, garyPokemon):
    if myPokemon == bulbasaur:
        specialMove = 'Vine Whip'
        specialMove2 = 'Razor Leaf'
    elif myPokemon == charmander:
        specialMove = 'Ember'
        specialMove2 = 'Flamethrower'
    elif myPokemon == squirtle:
        specialMove = 'Bubblebeam'
        specialMove2 = 'Water Gun'
    time.sleep(1)
    print("\033[2J\033[0;0H")
    print('___  __ )__    |__  __/__  __/__  /___  ____/')
    print('__  __  |_  /| |_  /  __  /  __  / __  __/   ')  
    print('_  /_/ /_  ___ |  /   _  /   _  /___  /___   ')
    print('/_____/ /_/  |_/_/    /_/    /_____/_____/   \n') 
    print(f'      {myPokemon} versus {garyPokemon}     {newL}') 
    time.sleep(1)
    firstAttack = input(f'{choicePrompt} {newL} {choice1} Tackle {newL} {choice2} Growl {newL} {choice3} {specialMove} {newL} {choice4} {specialMove2} {newL}' )
    if firstAttack == '1':
        print(f"{myPokemon} tackles Gary's {garyPokemon} and inflicts some damage")
    if firstAttack == '2':
        print(f"{myPokemon} 2nd attack Gary's {garyPokemon} and inflicts some damage")
    if firstAttack == '3':
        print(f"{myPokemon} 3rd attack Gary's {garyPokemon} and inflicts some damage")
    if firstAttack == '4':
        print(f"{myPokemon} yawns at Gary's {garyPokemon}. It's not very effective")

#Choice 5: Gary's Challenge
def garyChallenge(myPokemon, garyPokemon):
    time.sleep(1)
    print(f'Before I go become the best trainer around, I want my {garyPokemon} to take out your puny {myPokemon}. Ready, {myName}?')
    time.sleep(1)
    input(f"{newL}Press enter to continue...")
    garyBattle(myPokemon, garyPokemon)

#Choice 4: Gary's Pokemon
def garyChooses(myPokemon, garyPokemon):
    time.sleep(1)
    if myPokemon == bulbasaur: 
        garyPokemon = charmander
    elif myPokemon == charmander: 
        garyPokemon = squirtle
    elif myPokemon == squirtle: 
        garyPokemon = bulbasaur
    print(f"Gary: Pshh.. And now that you've chosen {myPokemon}, I'll take the real best Pokemon.{newL}")
    time.sleep(1)
    print(f"Gary chooses {garyPokemon}.{newL}")
    time.sleep(2)
    print(f"Gary: {garyPokemon}, welcome to the All Star team.{newL}")
    garyChallenge(myPokemon, garyPokemon)

#Choice 3: Choose your Pokemon
def choosePokemon(myPokemon):
    choosePoke = input(f'{choicePrompt} {newL} {choice1} The grass type {bulbasaur} {newL} {choice2} The fire type {charmander} {newL} {choice3} The water type {squirtle} {newL}' )
    if choosePoke == '1':
        myPokemon = bulbasaur
    elif choosePoke == '2':
        myPokemon = charmander
    elif choosePoke == '3':
        myPokemon = squirtle
    time.sleep(1)
    print(f"You've chosen {myPokemon}{newL}")
    garyChooses(myPokemon, garyPokemon)

#Choice 2: The Lab
def lateLab():
    print("\033[2J\033[0;0H")
    print('\nYou arrive at the lab and find the Professor standing by himself\n')
    time.sleep(1)
    print(f'Oak: What took you so long {myName}!')
    time.sleep(1)
    print(f"{newL}The three main Pokemon are gone. No more {bulbasaur}, {charmander}, or {squirtle}")
    time.sleep(2)
    print('\nBut there is another...\n')
    time.sleep(1)
    print(f'All of a sudden, there is a {pikachu} sitting next to you.')


def labStart():
    print('\nYou arrive at the lab and find the professor standing with his grandson.\n')
    time.sleep(1)
    print(f'Gary: Look who finally showed up. Hurry up and choose, {myName}.')
    time.sleep(1)
    print('\nYou walk up to the professor\'s counter. Whom will you choose?\n')
    time.sleep(2)   
    choosePokemon(myPokemon)

#
#Choice 1: Waking up
def startIntro():
    print('\n\033[3mbuzz\033[0m')
    time.sleep(1)
    print('\n\033[3mbuzz buzz\033[0m \n ')
    time.sleep(1)
    print(f"Mom: Wake up, {myName}! It's {day}!")
    time.sleep(1)
    print('\nMom: Did you hear me?! \n')
    time.sleep(1)

startIntro()

def wakeUp():
    print("\033[2J\033[0;0H")
    time.sleep(1)
    print("...\n")
    time.sleep(1)
    print(".....\n")
    time.sleep(1)
    print(f"{myName}: I'm up")
    time.sleep(1)
    print("\nMom: Don't be late. Professor Oak is waiting for you.\n")
    time.sleep(1)
    print("You run to the professor's lab.")
    time.sleep(1)
    labStart()

def staySleep2():
    print("\033[2J\033[0;0H")
    wakeUpResponse2 = input(f'{choicePrompt} {newL} {choice1} wake up {newL} {choice2} stay sleeping {newL}' )
    if wakeUpResponse2 == '1':
        wakeUp()
    
    elif wakeUpResponse2 == '2':
        print("\033[2J\033[0;0H")
        print('ZZzzZZZzzZzz\n')
        time.sleep(1)
        print("...\n")
        time.sleep(1)
        print('THE PROFESSOR!!! \n')
        print('You spring up from your bed and run to the lab in your pajamas')
        lateLab()

def staySleep1():
    print("\033[2J\033[0;0H")
    print("...\n")
    time.sleep(1)
    print(".....\n")
    time.sleep(1)
    print('just few more minutes...\n')
    staySleep2()

wakeUpResponse = input(f'{choicePrompt} {newL} {choice1} wake up {newL} {choice2} stay sleeping {newL}' )
if wakeUpResponse == '1':
    wakeUp()
    
elif wakeUpResponse == '2':
    print("\033[2J\033[0;0H")
    time.sleep(1)
    print('few more minutesszzzZzzZ')
    staySleep1()

######################################


#prompt for command option with list