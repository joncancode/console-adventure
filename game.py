import time
import datetime
import os

print("\033[2J\033[0;0H")
print("\t****************************")
print("\t***  \033[1;34mTitle of the égame!\033[0m  ***")
print("\t****************************")
time.sleep(2)

myName = input('What\'s your name? ')


print('\nGreat. Let\'s begin')
time.sleep(2)
print("\033[2J\033[0;0H")

dayOfWeek = datetime.datetime.today().weekday()

if dayOfWeek == 0:
    day = '\033[34mMonday\033[0m'
elif dayOfWeek == 1:
    day = '\033[34mTuesday\033[0m'
elif dayOfWeek == 2:
    day = '\033[34mWednesday\033[0m'
elif dayOfWeek == 3:
    day = '\033[34mThursday\033[0m'
elif dayOfWeek ==4:
    day = '\033[34mFriday\033[0m'
elif dayOfWeek == 5:
    day = '\033[34mSaturday\033[0m'
elif dayOfWeek == 6:
    day = '\033[34mSunday\033[0m'

def startIntro():
    print('Wake up, ' + myName + '! It\'s ' + day + '!')
    print(f"Wake up, {myName}!")

    time.sleep(2)
    print('Did you hear me?!')

startIntro()

# main()


#prompt for command option with list