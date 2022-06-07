from .TextKit import cprint
from .BackgroundKit import bgcolor
from .ColorKit import *

def version():
    print('Current Version: 0.1')

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
