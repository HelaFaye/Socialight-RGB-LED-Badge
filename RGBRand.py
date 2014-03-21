# make it easier to use random because it is the most important portion of this code
import random as R
# open a log file for appending
file = open('randrgb', 'a')
# predefine 'old' RGB values to conform to syntax
redold = R.randint(0,255)
greenold = R.randint(0,255)
blueold = R.randint(0,255)
# define a function for determining new RGB values and logging them
def RGBDo(redold,greenold,blueold):
    # randomize RGB values and average them with the previous ones
    redv = int(((R.randint(0,255)+redold)/2))
    greenv = int(((R.randint(0,255)+greenold)/2))
    bluev = int(((R.randint(0,255)+blueold)/2))
    # set old values for next run
    redold = redv
    greenold = greenv
    blueold = bluev
    # make tuple of RGB values for potential use
    RGBRand = (redv, greenv, bluev)
    # use tuple here just because it isn't yet used for anything else
    RGBRandstr = str((RGBRand))
    # write to log
    file.write(RGBRandstr)
    file.write('')
    # show what is being written
    print(RGBRand)
# repeat function
for i in range(9998):
    RGBDo(redold,greenold,blueold)
# close file properly
file.close()
