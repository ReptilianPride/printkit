from .TextKit import cprint
from .BackgroundKit import bgcolor
from .ColorKit import *

#for windows support
import os
os.system('')

def version():
    print('Current Version: 0.1.3')

def colors():
    availableColors=[
        'default',
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'lightgrey',
        'darkgrey',
        'lightred',
        'lightgreen',
        'lightyellow',
        'lightblue',
        'lightmagenta',
        'lightcyan',
        'white'
    ]
    for i in range(0,len(availableColors)):
        print("--->  {}".format(availableColors[i]))
