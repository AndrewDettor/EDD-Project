# youNeedHelpUpgrading.py v0.1
import sys
import time
import os
import subprocess
from scipy import stats

CPU = input('Enter CPU Score: ')
while type(CPU) is not int:
    try:
        CPU = int(CPU)
    except Exception as e:
        CPU = input('"' + e + '"' + ' is not an integer value, try again: ')

ThreeD = input('Enter 3D Score: ')
while type(ThreeD) is not int:
    try:
        ThreeD = int(ThreeD)
    except Exception as e:
        ThreeD = input("'" + e + "'" + ' is not an integer value, try again: ')

Disk = input('Enter Disk Score: ')
while type(Disk) is not int:
    try:
        Disk = int(Disk)
    except Exception as e:
        Disk = input("'" + e + "'" + ' is not an integer value, try again: ')

TwoD = input('Enter 2D Score: ')
while type(TwoD) is not int:
    try:
        TwoD = int(TwoD)
    except Exception as e:
        TwoD = input("'" + e + "'" + ' is not an integer value, try again: ')

Memory = input('Enter Memory Score: ')
while type(Memory) is not int:
    try:
        Memory = int(Memory)
    except Exception as e:
        Memory = input("'" + e + "'" + ' is not an integer value, try again: ')

PassMark = input('Enter PassMark Score: ')
while type(PassMark) is not int:
    try:
        PassMark = int(PassMark)
    except Exception as e:
        PassMark = input("'" + e + "'" + ' is not an integer value, try again: ')

# Constant * Weighted Harmonic Mean
equation = int(round(1 / (((1 / (CPU * 0.396566187)) + (1 / (TwoD * 3.178718116)) + (1 / (ThreeD * 2.525195879)) + (1 / (Memory * 1.757085479)) + (1 / (Disk * 1.668158805)))/5)))
whm = stats.hmean([CPU * 0.396566187, TwoD * 3.178718116, ThreeD * 2.525195879, Memory * 1.757085479, Disk * 1.668158805])

if equation != PassMark:
    print('You have entered your individual scores incorrectly, restarting program.')
    time.sleep(1)
    os.execl(sys.executable, sys.executable, *sys.argv) #wont work if .py file's path is stored in a directory with a ' ', try subprocesses, like subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"') NOTE: could create infinite process until out of memory

# Quantify preformance
performance = 0
if PassMark < 1260:
    performance = 1
elif PassMark < 3500:
    performance = 2
elif PassMark < 5200:
    performance = 3
else:
    performance = 4

# https://www.pcbenchmarks.net/builder.php

# What preformance do they want
use = input('What do you wish to use your computer for? \n (1)Web browsing / Office \n (2)Video Games \n (3)Workstation \nChoice: ')
while type(use) is not int:
    try:
        use = int(use)
        while (use in [1,2,3]) == False:
            use = int(input('Not an option, try again: '))
    except:
        use = int(input('Not an option, try again: '))

if use == 2:
    level = input('At medium settings, what framerate do you hope to achieve? \n (1)30 fps \n (2)60 fps \n (3)144 fps \nChoice:  ')
    while type(level) is not int:
        try:
            level = int(level)
            while level in [1,2,3] == False:
                level = int(input('Not an option, try again: '))
        except:
            level = input('Not an option, try again: ')
    if level > 1:
        use = 3
elif use == 3:
    level = input('What do you use your workstation for? \n (1)Rendering 1080p Footage (2)Rendering 4K Footage (3)AutoDesk Applications (4)VMs (5)Listen bro, I just work here and they give me this hunk of metal \nChoice:')
    while type(level) is not int:
        try:
            level = int(level)
            while level in [1,2,3,4,5] == False:
                level = int(input('Not an option, try again: '))
        except:
            level = input('Not an option, try again: ')
    if level < 5:
        use = 4

# Return where there computer is preforming
if performance >= use:
    print('Your computer is capable of the tasks you require of it.')
else:
    print('Your computer should be upgraded to more adequately fufill the tasks required of it.')
    # this is where it would call the other parts of the program
